import time
import pyautogui as pg
import random

# Define imageOffset and wt here
imageOffset = 25
wt = random.uniform(5, 6)

class MapPaths:
    U = (980, 29)
    D = (937, 910)
    R = (1562, 458)
    L = (355, 459)


class Bot:

    def pnj_tp_fri3_tremble(self):
        
        time.sleep(wt)
        pg.click(1021, 637)
        time.sleep(wt)

        pg.click(954, 744)
        time.sleep(wt)


class Fight:

    def fight_detect(self):
        try: 
            pos = pg.locateOnScreen("fight.png", confidence=0.8)  # Adjusted confidence threshold
            if pos is not None:
                    pg.click(1448, 1004)
                    time.sleep(wt)
                    pg.click(867, 570)
            else:
                print("No fight right now")
        except Exception as e:
            print(f"An error occurred: {e}")


class Tremble:

    def ressource_tremble(self):
        try: 
            pos = pg.locateOnScreen("tremble.png",confidence=0.9)
            pg.moveTo(pos[0] + imageOffset, pos[1] + imageOffset)
            pg.click()
            time.sleep(wt)
        except:
            print("Tremble not found")
        



# Create instances of the classes
map_paths = MapPaths()
bot = Bot()
tremble = Tremble()
fight = Fight()



