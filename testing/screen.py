import os
import pyautogui
import keyboard
from datetime import datetime

# Define the folder where your custom screenshots will be saved
output_folder = "custom_screenshots"

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Define a function to take and save a screenshot
def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{timestamp}.png"
    screenshot_path = os.path.join(output_folder, screenshot_name)
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {screenshot_name}")


# Register a hotkey (Ctrl+PrintScreen) to trigger the screenshot
keyboard.add_hotkey("ctrl+print screen", take_screenshot)

# Prevent the default behavior of taking a screenshot with Ctrl+PrintScreen
keyboard.hook_key("print screen", lambda e: None)

print("Press Ctrl+PrintScreen to take a custom screenshot. Press Ctrl+C to exit.")

keyboard.wait("ctrl+c")  # Wait for Ctrl+C to exit the program
