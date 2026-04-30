import os
import sys
import subprocess
import shutil
from download_ffmpeg import download_ffmpeg

def create_icons(png_path):
    """Convert PNG to ICO and ICNS for the app."""
    if not os.path.exists(png_path):
        print(f"⚠️  Icon {png_path} not found. Skipping icon creation.")
        return None, None

    print("🎨 Creating app icons...")
    
    ico_path = "icon.ico"
    icns_path = "icon.icns"

    try:
        from PIL import Image
        # Create ICO for Windows
        img = Image.open(png_path)
        img.save(ico_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
        
        # Create ICNS for Mac (using system tools)
        if sys.platform == "darwin":
            iconset_dir = "icon.iconset"
            os.makedirs(iconset_dir, exist_ok=True)
            sizes = [16, 32, 64, 128, 256, 512, 1024]
            for size in sizes:
                subprocess.run(['sips', '-z', str(size), str(size), png_path, '--out', f"{iconset_dir}/icon_{size}x{size}.png"], capture_output=True)
                if size <= 512:
                    subprocess.run(['sips', '-z', str(size*2), str(size*2), png_path, '--out', f"{iconset_dir}/icon_{size}x{size}@2x.png"], capture_output=True)
            
            subprocess.run(['iconutil', '-c', 'icns', iconset_dir], capture_output=True)
            shutil.rmtree(iconset_dir)
        
        return ico_path, icns_path
    except Exception as e:
        print(f"⚠️  Could not create icons: {e}")
        return None, None

def build():
    print("🚀 Starting Icarus A Build Process...")
    
    # 1. Ensure FFmpeg is ready
    download_ffmpeg()
    
    # 2. Handle Icons
    ico, icns = create_icons("cloud-download.png")
    icon_file = icns if sys.platform == "darwin" else ico

    # 3. PyInstaller command
    separator = os.pathsep
    cmd = [
        'pyinstaller',
        '--noconsole',
        '--onedir',
        '--clean',
        f'--add-data=templates{separator}templates',
        f'--add-data=static{separator}static',
        f'--add-data=bin{separator}bin',
        '--name=Icarus A',
        'main.py'
    ]

    if icon_file and os.path.exists(icon_file):
        cmd.insert(1, f'--icon={icon_file}')

    print(f"📦 Running command: {' '.join(cmd)}")
    subprocess.run(cmd)

    print("\n✅ Build Successful!")
    print("📂 Your software is ready in the 'dist' folder.")
    print("👉 Look for 'Icarus A.app' (Mac) or 'Icarus A' folder (Windows)")

if __name__ == "__main__":
    build()
