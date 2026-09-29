# Write your code here :-)
from microbit import *

def show_scroll(msg):
    display.scroll(msg)

count=0
while True:
    if button_a.is_pressed():
        count = count +1
        show_scroll(count)
    if button_b.was_pressed():
        count=0
        show_scroll("reset")
    sleep(200)
    button_a.

