/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Noah Yang
 * Created on: Feb 2026
 * This program tells the current temperature
*/

// The Variable For Temperature
let currentTemperature: number

// Preparation
basic.clearScreen()
basic.showIcon(IconNames.Happy)
basic.pause(500)

// The Procedure
input.onButtonPressed(Button.A, function () {
  currentTemperature = input.temperature()
  basic.showString('The temperature is ' + currentTemperature)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})
