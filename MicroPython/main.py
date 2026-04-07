"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *


# setup before a is pressed

display.clear()

display.show(Image.HAPPY)

sleep(1000)


# calculates temp then shows it

while True:

    if button_a.was_pressed():

        temperature = temperature()

        display.scroll("The temperature is " + (temperature))

        display.clear()

        display.show(Image.HAPPY)

        sleep(1000)
