# Write your code here :-)
from microbit import *

list=[12,14,16]



for i in range(len(list)):
    x = list[i] + 1
    list.append(x)
    display.scroll(x)
