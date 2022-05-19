import pyautogui as pog
import time
import keyboard


def egg():
    """
    The main function to migrate videos.
    """
    # These upcoming button clicks are to add the current video to the new playlist.
    # Looks for the save button and clicks it.
    pog.click(pog.locateCenterOnScreen('Save.png', grayscale=True))

    time.sleep(.5)

    # Looks for the new playlist button and clicks it.
    pog.click(pog.locateCenterOnScreen('New_playlist.png', grayscale=True))

    time.sleep(.5)

    # Looks for the exit button and clicks it.
    pog.click(pog.locateCenterOnScreen('Exit.png', grayscale=True))

    time.sleep(.5)

    # These next button presses are to go to the next video.
    # Presses and holds shift.
    pog.keyDown('shift')

    time.sleep(.5)

    # Presses n.
    pog.press('n')

    time.sleep(.5)

    # Releases shift.
    pog.keyUp('shift')


# Creates a loop that will run the egg function until the the escape key is pressed.
while True:
    egg()
    # Checks if the escape key is pressed.
    if keyboard.is_pressed('esc'):
        print("Escape key pressed.")
        break
