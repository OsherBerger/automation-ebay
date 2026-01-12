import os
import subprocess
import zipfile
import urllib.request
import shutil
import winreg

# הגדרות
ALLURE_DIR = "C:\\allure"  # איפה ש-Allure יותקן
ALLURE_ZIP_URL = "https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.zip"

def is_allure_in_path():
    try:
        subprocess.run(["allure", "--version"], check=True, capture_output=True)
        return True
    except Exception:
        return False

def download_and_extract_allure():
    print("Downloading Allure...")
    zip_path = os.path.join(os.getcwd(), "allure.zip")
    urllib.request.urlretrieve(ALLURE_ZIP_URL, zip_path)
    print("Extracting Allure...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        if os.path.exists(ALLURE_DIR):
            shutil.rmtree(ALLURE_DIR)
        zip_ref.extractall(ALLURE_DIR)
    os.remove(zip_path)
    print(f"Allure extracted to {ALLURE_DIR}")

def add_to_system_path(bin_path):
    # פותח את ה-Registry ומוסיף את Allure ל-PATH של המשתמש
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        r'Environment',
                        0,
                        winreg.KEY_READ | winreg.KEY_WRITE) as key:
        try:
            current_path, _ = winreg.QueryValueEx(key, 'Path')
        except FileNotFoundError:
            current_path = ''
        if bin_path not in current_path:
            new_path = current_path + ";" + bin_path if current_path else bin_path
            winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path)
            print(f"✅ Added {bin_path} to PATH permanently.")
        else:
            print("Allure path already in PATH.")

if __name__ == "__main__":
    bin_path = os.path.join(ALLURE_DIR, "bin")
    
    if not os.path.exists(bin_path):
        download_and_extract_allure()

    add_to_system_path(bin_path)
    
    print("⚠️ You must restart your terminal or PC for PATH changes to take effect.")
    print("After restarting, run: allure --version")
