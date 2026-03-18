# Image-Based Clicking Bot
This script is a simple image‑recognition auto‑click bot built with PyAutoGUI. It continuously scans the screen for a specific image and automatically clicks on it whenever it appears.
The bot uses a reference image named `imagen.png`, which is included in this folder as an example. You can replace it with any other image as long as it has the same filename.

## Flow (Requires PyAutoGU)
- The script loads a target image (imagen.png).
- It repeatedly searches the entire screen for that image using pyautogui.locateCenterOnScreen().
- When a match is found (with Y% confidence), the bot clicks on the detected coordinates.
- The process repeats every X seconds.
- You can stop the bot safely at any time using CTRL + C.
