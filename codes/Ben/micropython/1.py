# Write your code here :-)
from microbit import *
def flash(image, times):
    for i in range(times):
        display.show(image)
        sleep(200)
        display.clear()
        sleep(200)

flash(Image.HEART, 3)
