
import cv2,pyautogui,pytesseract,os
import numpy as np   
tesseract_path = rf'C:\Program Files\Tesseract-OCR\tesseract.exe'  

# Check if the file exists  

pytesseract.pytesseract.tesseract_cmd = tesseract_path

def on_screen_img_coordinate(screenshot_rgb,search_img,center_coordinate=False):
    # Convert the screenshot to a numpy array
    """ 
    Args:
    screenshot_rgb (numpy.ndarray): screenshot image
    search_img (numpy.ndarray): search image
    center_coordinate (bool): whether to return the center coordinate of the search image. Defaults to False
    Returns:
    numpy.ndarray: the coordinate of the search image in the screenshot image

    """
    try:
        screenshot_np = np.array(screenshot_rgb)
        screen_img = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        small_image = cv2.imread(search_img)
        if screen_img is None or small_image is None:  
            print("Could not load one or both images. Please check the paths.")  
        else:  
            small_height, small_width = small_image.shape[:2]  

            result = cv2.matchTemplate(screen_img, small_image, cv2.TM_CCOEFF_NORMED)  
            threshold = 0.8  # Adjust threshold as necessary  
            locations = np.where(result >= threshold)  
            match_coordinates = []
            return_data=[]
            # If a matching location is found  
            if locations[0].size > 0:  
                # print(f"{len(locations[0])} matches found!")

                for pt in zip(*locations[::-1]):  # Switch columns and rows  
                    # Draw a rectangle around each matched region  
                    cv2.rectangle(screen_img, pt, (pt[0] + small_width, pt[1] + small_height), (0, 255, 0), 2)  
                    match_coordinates.append([int(pt[0]),int(pt[1])])

            # else:  
            #     print("No match found.")
            if center_coordinate:
                for coord in match_coordinates:
                    # print(coord[0] + small_width // 2, coord[1] + small_height // 2)
                    return_data.append([int(coord[0]) + small_width // 2, int(coord[1]) + small_height // 2])
                    # print(return_data)
            else:
                return_data=match_coordinates.copy()[0]
            return return_data
    except Exception as e :
        print(f"Error: {e }")
        return None
def text_to_cordnite(word_to_find):
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert('RGB')
    data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    coordinates = []
    print(data)

    for i, word in enumerate(data['text']):
        if word.lower() == word_to_find.lower():  # Case-insensitive search
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            
            # Append the coordinates (x, y) and size (width, height) of the word
            coordinates.append((x, y))
    return coordinates
