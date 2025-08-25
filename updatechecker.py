import requests
import os

APP_VERSION = "4.1"
VERSION_URL = "https://raw.githubusercontent.com/fariesabdullah/Number-Converter-/refs/heads/main/version.json"

def check_for_update():
    try:
        response = requests.get(VERSION_URL, timeout=5)
        data = response.json()
        latest_version = data["version"]
        print(latest_version)
        if latest_version > APP_VERSION:
            print(f"Update available: {latest_version}")
            print("Release notes:\n", data.get("notes", ""))
            return True, data
        else:
            print("You are up to date.")
            return False, data
    except Exception as e:
        print("Failed to check for updates:", e)
        return False, {}

def download_update(url, filename="numberconverter.exe"):
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))  # total size in bytes
    downloaded = 0

    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)

                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    yield percent
                    #print(f"\rDownloading... {percent:.2f}%", end="", flush=True)
    yield 100.0
    print("\nDownload complete. Starting installer...")
    os.startfile(filename)
    

#update, data = check_for_update()

#download_update(data["url"])