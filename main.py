import os
import sys
import threading
import time
import socket
import webbrowser
import subprocess
from app import app

def show_mac_error(error_msg):
    """Show a native macOS alert dialog with the error."""
    script = f'display alert "Icarus A Error" message "{error_msg}" as critical'
    subprocess.run(['osascript', '-e', script])

def get_free_port():
    """Find an available port on localhost."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 0))
        port = s.getsockname()[1]
        s.close()
        return port
    except Exception as e:
        show_mac_error(f"Socket Error: {str(e)}")
        sys.exit(1)

def start_flask(port):
    """Start the Flask server."""
    try:
        app.run(host='127.0.0.1', port=port, debug=False, use_reloader=False)
    except Exception as e:
        show_mac_error(f"Server Error: {str(e)}")

def open_window(url):
    """Opens the URL in a dedicated app-like window."""
    # Common paths for Chrome/Edge on Mac and Windows
    browser_paths = [
        # macOS
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
        '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
        # Windows
        os.path.expandvars(r'%ProgramFiles%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%ProgramFiles%\Microsoft\Edge\Application\msedge.exe'),
        os.path.expandvars(r'%LocalAppData%\Google\Chrome\Application\chrome.exe')
    ]
    
    opened = False
    for path in browser_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path, f'--app={url}'])
                opened = True
                break
            except Exception:
                continue
    
    if not opened:
        webbrowser.open(url)

def main():
    try:
        # 1. Get an available port
        port = get_free_port()
        url = f'http://127.0.0.1:{port}'

        # 2. Start Flask in a background thread
        t = threading.Thread(target=start_flask, args=(port,))
        t.daemon = True
        t.start()

        # 3. Wait for server to initialize
        time.sleep(1.5)

        # 4. Launch the interface window
        open_window(url)

        # 5. Keep the main thread alive
        while True:
            time.sleep(1)
            
    except Exception as e:
        show_mac_error(f"Startup Crash: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
