import time
import pyautogui
import keyboard

purchased = 0
missed = 0



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


print("Starting in 3 seconds...")
time.sleep(3)



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
        time.sleep(0.85)
            
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
            success = pyautogui.locateOnScreen(
                "imgs/success.png",
                confidence=0.6
            )
            fail = pyautogui.locateOnScreen(
                "imgs/failed.png",
                confidence=0.6
            )
            if fail:
                print("Couldn't buy out...")
                missed = missed+1
                print("Current missed:",missed)
                print("Current Brought",purchased)
                print("Current Success Rate: "+str((purchased/(purchased+missed)*100))+"%")
                pyautogui.press("enter")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("enter")
            elif success:
                print("Purhcased!")
                purchased = purchased+1
                print("Current missed:",missed)
                print("Current Brought",purchased)
                if purchased == 0 or missed == 0:
                    print("Current Success Rate: 0%")
                else:
                    print("Current Success Rate: "+str((purchased/(purchased+missed)*100))+"%")
                pyautogui.press("enter")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("enter")
            else:
                print("ERROR, idfk")
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("enter")
                
        elif pyautogui.pixel(233,228) == (234, 222, 0):
            print("Car Sold...")
            pyautogui.press("esc")
            time.sleep(1)
            pyautogui.press("enter")

        
    else:
        print("Not found")


