# YouTube Downloader Pro - Desktop Software Guide

This guide explains how to use and build your standalone YouTube Downloader software.

## 🚀 How to Run (Development)

If you have Python installed and want to run it without building the software first:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python main.py
   ```
This will open the app in a dedicated window instead of your browser.

## 📦 How to Build the Standalone Software

To create a single file (`.app` for Mac or `.exe` for Windows) that you can send to anyone:

1. Open your terminal in this folder.
2. Run the build script:
   ```bash
   python build_app.py
   ```
3. Wait for it to finish. 
4. Open the **`dist`** folder. Your software is there!

## ⚠️ Important: FFmpeg

The software needs **FFmpeg** to merge high-quality video and audio. 
- **On Mac:** Most users have it or can install it with `brew install ffmpeg`.
- **On Windows:** Ensure `ffmpeg.exe` is in the user's system PATH.

## 📁 Where are downloads saved?

By default, the software saves all videos to your computer's main **Downloads** folder in a subfolder named `YouTube-Downloads`.
