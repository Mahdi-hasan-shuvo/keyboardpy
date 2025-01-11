
# from keyboard import *
import os
from .img_screen import get_window_img,screenshot_app_by_name
from .cordinate import text_to_cordnite,on_screen_img_coordinate
from .installer_tesseract import *
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

# Check if the file exists  
if os.path.exists(tesseract_path):
    pass
    # print("Tesseract-OCR is installed and ready to use!")
else:
    install_tesseract()
