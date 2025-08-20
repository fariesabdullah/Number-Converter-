import requests
import os

APP_VERSION = "2.1"
VERSION_URL = "https://github.com/fariesabdullah/Number-Converter-/blob/main/version.json"

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

def download_update(url, filename="update.exe"):
    print("Downloading update...")
    response = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print("Download complete. Starting installer...")
    os.startfile(filename)

check_for_update()