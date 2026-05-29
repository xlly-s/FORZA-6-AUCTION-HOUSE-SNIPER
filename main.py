import time
import pyautogui
import keyboard

SEARCHREGION = (537, 294, 1376, 387)
NOAUCTIONSREGION = (977,168,1825,944)
SOLDREGION = (119, 212, 263, 271)
AVAILABLEREGION = (898,617,1458,888)

CONFIDENCE = 0.82
CHECK_DELAY = 0.15

running = True



def stop():
    global running
    running = False
    print("Stopped.")

keyboard.add_hotkey("ctrl+c", stop)




def exists(img, region=None):
    return pyautogui.locateOnScreen(
        img,
        confidence=CONFIDENCE,
        region=region
    )


print("Starting in 10 seconds...")
time.sleep(10)



while running:
    searchbox = pyautogui.locateOnScreen(
        "imgs/searchmenu.png",
        confidence=0.8,
        region=SEARCHREGION,
        grayscale=True
    )

    player = pyautogui.locateOnScreen(
        "imgs/playeroptions.png",
        confidence=0.7
    )

    if player:
        print("ERROR, ENDED UP ON PLAYER SCREEN")
        pyautogui.press("esc")
        time.sleep(0.5)
        pyautogui.press("esc")
        time.sleep(0.5)
        pyautogui.press("esc")
        time.sleep(0.5)
        

    if searchbox:
        print("Search menu opened:", searchbox)
        pyautogui.press("enter")
        time.sleep(0.5)
            
        noauctions = pyautogui.locateOnScreen(
            "imgs/noauctions.png",
            confidence=0.5,
            region=NOAUCTIONSREGION,
            grayscale=False
        )
        available = pyautogui.locateOnScreen(
            "imgs/open.png",
            confidence=0.4,
            region=AVAILABLEREGION,
            grayscale=False
        )
        

        time.sleep(0.5)
        if pyautogui.pixel(1210, 540) == (255, 255, 255):
            print("No cars:",noauctions)
            pyautogui.press("esc")
            time.sleep(1)
            pyautogui.press("enter")
            continue
        elif pyautogui.pixel(233,228) != (234, 222, 0):
            pyautogui.press("y")
            time.sleep(0.1)
            pyautogui.press("down")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(4)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("esc")
            time.sleep(0.2)
            pyautogui.press("esc")
            time.sleep(1)
            pyautogui.press("enter")
        else:
            print("unknown, returning")
            pyautogui.press("esc")
            time.sleep(1)
            pyautogui.press("enter")

        
    else:
        print("Not found")


