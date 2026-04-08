"""
Created by: Noah
Created on: Feb 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *

# variable
temperatureInRoom = 0
# setup before a is pressed
display.clear()
display.show(Image.HAPPY)

sleep(1000)

# calculates temp then shows it
while True:
    if button_a.was_pressed():
        temperatureInRoom = temperature()
        display.scroll("The temperature is")
        display.scroll(temperatureInRoom)
        display.clear()
        display.show(Image.HAPPY)
        sleep(1000)
