
import pygetwindow as gw
import pyautogui
import time
def get_window_img():
    screenshot = pyautogui.screenshot()
    screenshot_rgb = screenshot.convert('RGB')
    return screenshot_rgb

def screenshot_app_by_name(exe_name, save_path=None):
    try:
        """ 
         :param exe_name: name of the application to be captured
         :param save_path: path to save the screenshot
        expline : This function takes the name of the application and saves the screenshot of the application
        example :
        screenshot_app_by_name("chrome.exe ")

        """
        window = gw.getWindowsWithTitle(exe_name)

        # Check if the window was found
        if window:
            window = window[0]  # Assuming there's only one window with this title
            
            # Step 2: Get the window's position and size (left, top, width, height)
            left, top, width, height = window.left, window.top, window.width, window.height
            
            # Step 3: Take a screenshot of the area (left, top, width, height)
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot_rgb = screenshot.convert('RGB')
            print("Screenshot saved successfully!")
            if save_path:
            # Step 4: Optionally, save the screenshot using Pillow
                screenshot.save(save_path)
            else:
                pass
            return screenshot_rgb
            
        else:
            ValueError ("Window not found")
            print("Window not found!")

    except Exception as e:
        print(f"Error: {e}")



