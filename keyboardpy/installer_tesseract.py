import re
import requests  
import os  
import subprocess  
import time  
import sys   
import ctypes 
# URL of the Tesseract OCR installer  
tesseract_url = "https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe"  
installer_name = "tesseract-ocr-setup.exe"  
# Download the installer
def install_tesseract():
    download_installer(tesseract_url, installer_name)
    run_installer(installer_name)
    if os.path.exists(installer_name):  
        os.remove(installer_name)  
        print("Installer deleted.")
def download_installer(url, filename):  
    print(f"Downloading {filename} from {url}...")  
    response = requests.get(url, stream=True)  # Stream the download  
    # Check if the request was successful  
    if response.status_code == 200:  
        total_size = int(response.headers.get('content-length', 0))  # Get total file size  
        block_size = 1024  # 1 KB  
        with open(filename, 'wb') as file:  
            # Download in chunks  
            for data in response.iter_content(block_size):  
                file.write(data)  
                # Calculate progress  
                downloaded_size = file.tell()  # Current file size  
                percentage = (downloaded_size / total_size) * 100 if total_size > 0 else 0  
                # Print progress  
                sys.stdout.write(f"\rDownloaded {str(filename).replace('.exe','')} {downloaded_size} of {total_size} bytes ({percentage:.2f}%)")  
                sys.stdout.flush()  
        print("\nDownload complete!")  
        return filename
    else:  
        print("Failed to download the installer. Status code:", response.status_code)  
def run_installer(filename):  
    """Run the installer with administrative privileges."""  
    print(f"Running the installer {filename} with administrative privileges...")  
    # Create a command to run the installer silently  
    command = f'"{filename}" /S'  # Ensure the command is properly quoted  
    # Use ShellExecute to run the installer with elevated permissions  
    try:  
        # The second argument 'runas' specifies that we want to run as an administrator  
        ctypes.windll.shell32.ShellExecuteW(None, "runas", filename, "/S", None, 1)  
        print("Installation process started.")  
    except Exception as e:  
        print(f"An error occurred while trying to run the installer: {e}")  
