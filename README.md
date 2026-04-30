# 🦅 Icarus A
**Premium Desktop YouTube Downloader for macOS & Windows**

Icarus A is a modern, standalone desktop application designed for high-speed, high-quality video and audio downloads. Built with a focus on simplicity and premium aesthetics, it handles complex tasks like 1080p video merging and MP3 conversion automatically.

![Icarus A Interface](static/images/logo.png) <!-- You can add a screenshot here later -->

## ✨ Features

### 🎥 Native Power
- **Standalone App**: No Docker or terminal setup needed. Just open the `.app` or `.exe`.
- **Apple Silicon Native**: Optimized for M1/M2/M3 chips (No Rosetta warning).
- **Auto-FFmpeg**: Automatically downloads and bundles its own processing engine.
- **Chrome App Mode**: Runs in a dedicated, sleek window without browser clutter.

### 💎 Premium Downloads
- **Ultra HD Support**: Downloads and merges 1080p and 4K videos with audio.
- **Instant MP3**: High-quality audio extraction with a single click.
- **Smart Progress**: Real-time progress tracking and status updates.
- **Visual History**: Manage your recent downloads with built-in thumbnails.
- **Global Downloads**: Saves files directly to your system `Downloads/Icarus-Downloads` folder.

## 🚀 Installation & Usage

### For Users
1. **Download**: Get the latest version from the **GitHub Actions** tab (Artifacts).
2. **Launch**:
   - **Mac**: Right-click `Icarus A.app` and select **Open**.
   - **Windows**: Open the `Icarus A` folder and run `Icarus A.exe`.
3. **Enjoy**: Paste a link and start downloading!

### For Developers
If you want to build the software locally:

1. **Setup Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac
   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   pip install Pillow
   ```

2. **Build the Desktop App**:
   ```bash
   python build_app.py
   ```
   The final app will be waiting in the `dist/` folder.

## 🛠 Tech Stack
- **Engine**: Python 3.9 + Flask (Internal Backend)
- **UI**: Glassmorphism CSS + Vanilla JavaScript
- **Processing**: FFmpeg (Bundled)
- **Packaging**: PyInstaller
- **CI/CD**: GitHub Actions (Multi-platform Builds)

## 📝 License
MIT License - Created for a premium downloading experience.
