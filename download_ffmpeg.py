import os
import sys
import requests
import zipfile
import shutil

def download_ffmpeg():
    print("Downloading portable FFmpeg...")
    
    bin_dir = os.path.join(os.getcwd(), "bin")
    os.makedirs(bin_dir, exist_ok=True)
    
    # Direct download link for the latest stable FFmpeg
    if sys.platform == "darwin":
        # Mac (Apple Silicon & Intel)
        url = "https://evermeet.cx/ffmpeg/getrelease/ffmpeg/zip"
    else:
        # Windows
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    
    local_zip = os.path.join(bin_dir, "ffmpeg.zip")
    
    if os.path.exists(os.path.join(bin_dir, "ffmpeg")):
        print("FFmpeg already exists in bin folder.")
        return

    try:
        # Download with headers to avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
        
        if response.status_code != 200:
            print(f"Download failed. Status code: {response.status_code}")
            return

        with open(local_zip, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*1024): # 1MB chunks
                if chunk:
                    f.write(chunk)
        
        print("Extracting...")
        if not zipfile.is_zipfile(local_zip):
            print("The downloaded file is corrupted or not a zip.")
            return

        with zipfile.ZipFile(local_zip, 'r') as zip_ref:
            zip_ref.extractall(bin_dir)
        
        # Cleanup zip
        os.remove(local_zip)
        
        # Organize binary
        if sys.platform == "darwin":
            # Search for ffmpeg file in extracted contents
            for root, dirs, files in os.walk(bin_dir):
                if "ffmpeg" in files and "ffmpeg.zip" not in files:
                    src = os.path.join(root, "ffmpeg")
                    dst = os.path.join(bin_dir, "ffmpeg")
                    if src != dst:
                        shutil.move(src, dst)
                    os.chmod(dst, 0o755)
                    print(f"FFmpeg moved to {dst}")
                    break
        
        print("FFmpeg setup complete!")
        
    except Exception as e:
        print(f"Failed to download FFmpeg: {e}")

if __name__ == "__main__":
    download_ffmpeg()
