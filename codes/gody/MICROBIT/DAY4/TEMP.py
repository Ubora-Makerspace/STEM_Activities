# Write your code here :-)

from microbit import *

while True:
    if (temperature()>32):
        display.show(Image.SAD)
    elif (temperature()<32):
        display.show(Image.SMILE)


