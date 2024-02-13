import time 
import random 
import pyautogui as pg 
from mappath import MapPaths , bot , tremble


wt = random.uniform(6, 7)


def woodpath(paths):

    pg.click(paths.U)
    time.sleep(wt)

    pg.click(paths.U)
    time.sleep(wt)

    pg.click(paths.U)
    time.sleep(wt)

    pg.click(paths.U)
    time.sleep(wt)

    pg.click(paths.U)
    time.sleep(wt)

    pg.click(paths.R)
    time.sleep(wt)

    pg.click(paths.R)
    time.sleep(wt)

    pg.click(paths.R)
    time.sleep(wt)

    pg.click(paths.R)
    time.sleep(wt)

    pg.click(paths.R)
    time.sleep(wt)

    pg.click(1287, 582)
    time.sleep(wt)

    woodpath(MapPaths)