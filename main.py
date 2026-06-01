import time
import pyautogui
import keyboard

purchased = 0
missed = 0



SEARCHREGION = (537, 294, 1376, 387)
NOAUCTIONSREGION = (977,168,1825,944)
SOLDREGION = (119, 212, 263, 271)
AVAILABLEREGION = (898,617,1458,888)



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
        

    if pyautogui.pixel(850, 329) == (202, 255, 2):
        print("Search menu opened:", searchbox)
        pyautogui.press("enter")
        auctionmenu = False
        options = 0
        while auctionmenu == False:
            if pyautogui.pixel(232,119) == (255, 255, 255):
                print("Options found")
                time.sleep(0.3)

                break
            else:
                print("No search options found...")
                options = options + 1
                if options == 100:
                    print("ERROR")
                    pyautogui.press("esc")
                    options = 0
                    continue
            
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
            mainmenuopen = False
            options = 0
            while mainmenuopen == False:
                if pyautogui.pixel(443,665) == (202, 255, 2):
                    print("Options found")
                    time.sleep(0.15)
                    pyautogui.press("enter")
                    break
                else:
                    print("No options found...")
                    options = options + 1
                    if options == 100:
                        print("ERROR")
                        pyautogui.press("esc")
                        options = 0
                        continue
                        
                    

            continue
        elif pyautogui.pixel(233,228) != (234, 222, 0):
            pyautogui.press("y")
            options = 0
            menuopen = False
            while menuopen == False:
                if pyautogui.pixel(1103,384) == (0,0,0) or pyautogui.pixel(826,436) == (0,0,0) or pyautogui.pixel(1288,427) == (202, 255, 2) or pyautogui.pixel(1249,405) == (202, 255, 2):
                    print("Options opened")
                    time.sleep(0.1)
                    break
                else:
                    print("No options found...")
                    options = options + 1
                    if options == 100:
                        print("ERROR")
                        pyautogui.press("esc")
                        options = 0
                        continue
                
                
            pyautogui.press("down")
            time.sleep(0.1)
            pyautogui.press("enter")
            buyoutmenuopen = False
            options = 0
            while buyoutmenuopen == False:
                if pyautogui.pixel(938,468) == (0,0,0):
                    print("Buyout opened")
                    time.sleep(0.02)
                    break
                else:
                    print("Waiting")
                    options = options + 1
                    if options == 100:
                        print("ERROR")
                        pyautogui.press("esc")
                        options = 0
                        continue
                    
                            
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
                options = 0
                mainmenuopen = False
                while mainmenuopen == False:
                    if pyautogui.pixel(443,665) == (202, 255, 2):
                        print("Options found")
                        time.sleep(0.15)
                        pyautogui.press("enter")
                        break
                    else:
                        print("No options found...")
                        options = options + 1
                        if options == 100:
                            print("ERROR")
                            pyautogui.press("esc")
                            options = 0
                            continue


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
                options = 0
                mainmenuopen = False
                while mainmenuopen == False:
                    if pyautogui.pixel(443,665) == (202, 255, 2):
                        print("Options found")
                        time.sleep(0.15)
                        pyautogui.press("enter")
                        break
                    else:
                        print("No options found...")
                        options = options + 1
                        if options == 100:
                            print("ERROR")
                            pyautogui.press("esc")
                            options = 0
                            continue


                pyautogui.press("enter")

            elif pyautogui.pixel(475, 766) == (60, 198, 79):
                print("Wrong Page... Reverting to search.")
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(0.5)
            else:
                print("ERROR, idfk")
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(0.2)
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(0.5)
                
        elif pyautogui.pixel(233,228) == (234, 222, 0):
            print("Car Sold...")
            pyautogui.press("esc")
            mainmenuopen = False
            options = 0
            while mainmenuopen == False:
                if pyautogui.pixel(443,665) == (202, 255, 2):
                    print("Options found")
                    time.sleep(0.15)
                    pyautogui.press("enter")
                    break
                else:
                    print("No options found...")
                    options = options + 1
                    if options == 100:
                        print("ERROR")
                        pyautogui.press("esc")
                        options = 0
                        continue
        
    elif pyautogui.pixel(475, 766) == (60, 198, 79):
        print("Wrong Page... Reverting to search.")
        pyautogui.press("esc")
        time.sleep(2)
        pyautogui.press("esc")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(0.5)
    else:
        print("Not found")


