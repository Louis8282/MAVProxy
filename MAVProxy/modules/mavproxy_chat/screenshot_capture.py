import os
import time
from datetime import datetime
from PIL import ImageGrab

def capture_screenshot(directory="./mavproxy_screenshots", filename="map_screenshot.jpeg"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
           # Assuming the full screen width is 1600 and height is 900
    # Adjust these values based on your actual screen resolution
    print(file_path)
    full_width = 1600
    full_height = 900
    left_x = 0
    top_y = 150  # Start 50 pixels down to skip the top strip
    right_x = full_width // 2  # Capture only the left half of the screen
    bottom_y = full_height - 20  # Stop 50 pixels before the bottom to skip the bottom strip

    # Define the screen region (left_x, top_y, right_x, bottom_y)
    bbox = (left_x, top_y, right_x, bottom_y)
    screenshot = ImageGrab.grab(bbox)
    # Save the screenshot as JPEG
    screenshot = screenshot.convert("RGB")  # Convert to RGB mode for JPEG
    screenshot.save(file_path, "JPEG", quality=40)  # Save as JPEG with quality 85
    full_path = os.path.abspath(file_path)
    print(f"Screenshot saved full path: {full_path}")

    print(f"Screenshot saved: {file_path}")

def wait_for_next_interval(interval=5):
    """ Wait until the next exact interval of N seconds (e.g., 0, 5, 10, 15, etc. seconds of any minute). """
    while True:
        now = datetime.now()
        remainder = now.second % interval
        if remainder == 0 and now.microsecond < 100000:  # Adjust microsecond threshold as needed
            break
        time.sleep(0.1)  # Check every 100 milliseconds to not miss the interval

def main():
    print("Current working directory:", os.getcwd())
    while True:
        wait_for_next_interval(5)  # Synchronize with 5-second intervals
        capture_screenshot()  # Capture and save screenshot
        time.sleep(4)  # Relax for 4 seconds after taking the screenshot

if __name__ == "__main__":
    main()
