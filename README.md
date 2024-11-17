# Screenshot and Image Matching Script Documentation

## Overview
This script utilizes the `pyautogui`, `opencv`, `numpy`, and `pygetwindow` libraries to capture screenshots of specific application windows and search for images within those screenshots. The script can return the coordinates of matched images and optionally save screenshots to a specified path.

## Requirements
- Python 3.x
- Libraries:
  - `opencv-python`
  - `numpy`
  - `pyautogui`
  - `pygetwindow`
  - `Pillow`

## Functions

### 1. `get_window_img()`
Captures a screenshot of the entire screen.

#### Returns:
- `PIL.Image`: A screenshot of the entire screen in RGB format.

---

### 2. `on_screen_img_coordinate(screenshot_rgb, search_img, center_coordinate=False)`
Searches for a specified image within a given screenshot and returns the coordinates of the matches.

#### Parameters:
- `screenshot_rgb` (PIL.Image): The screenshot in which to search for the image.
- `search_img` (str): The file path of the image to search for.
- `center_coordinate` (bool, optional): If `True`, returns the center coordinates of the matched images. Defaults to `False`.

#### Returns:
- `list`: A list of coordinates where the image was found. Each coordinate is represented as a list of `[x, y]`. If `center_coordinate` is `True`, the coordinates will be the centers of the matched images.

---

### 3. `screenshot_app_by_name(exe_name, save_path=None)`
Captures a screenshot of a specified application window by its title.

#### Parameters:
- `exe_name` (str): The title of the application window to capture.
- `save_path` (str, optional): The file path where the screenshot will be saved. If not provided, the screenshot will not be saved.

#### Returns:
- `PIL.Image`: A screenshot of the specified application window in RGB format. Returns `None` if the window is not found.

#### Raises:
- `Exception`: If an error occurs while capturing the screenshot.

---

## Usage Example

```python
# Import necessary libraries
import cv2
import pyautogui
import numpy as np
import pygetwindow as gw

# Take a screenshot of the entire screen
screenshot = get_window_img()

# Search for an image in the screenshot
matches = on_screen_img_coordinate(screenshot, 'path_to_image.png', center_coordinate=True)

# Take a screenshot of a specific application window
app_screenshot = screenshot_app_by_name('Application Title', save_path='screenshot.png')
