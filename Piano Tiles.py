from pynput.mouse import Button, Controller
from PIL import ImageGrab, Image
import cv2
import time
import numpy as np
from mss import mss
import pyautogui as auto


def press(tile):
    buttons = {"tile_1": (691, 862), "tile_2": (885, 862), "tile_3": (1055, 862), "tile_4": (1189, 862)}
    #auto.moveTo(buttons[tile])
    mouse.position = buttons[tile]
    mouse.click(Button.left, 1)
    print('Here in ', tile)
    #print(mouse.position)


def longPress(tile):
    pass

time.sleep(3)

with mss() as sct:
    monitor = {"top": 600, "left": 640, "width": 650, "height": 250}
    img = sct.grab(monitor)

img = np.array(img, dtype="uint8")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row = img[248:249]
tile_1 = int(row.shape[1] / 4 - 15)
tile_2 = tile_1 * 2
tile_3 = tile_1 * 3
tile_4 = tile_1 * 4

mouse = Controller()

c = 0
name = ''

while True:
    with mss() as sct:
        monitor = {"top": 600, "left": 640, "width": 650, "height": 250}
        img = cv2.cvtColor(np.array(sct.grab(monitor), dtype="uint8"), cv2.COLOR_BGR2GRAY)

    row = img[248:249]

    if row[:,tile_1] < 70:
        press('tile_1')

    elif row[:,tile_2] < 70:
        press('tile_2')

    elif row[:,tile_3] < 70:
        press('tile_3')

    elif row[:,tile_4] < 70:
        press('tile_4')

