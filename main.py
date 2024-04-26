'''
Automatic Clicker

This script allows you to perform a triple click automatically when a certain key is pressed.

Usage:
1. Run the script.
2. Enter the key to activate the program.
3. Enter the key to disable the program.

The keys must be specified in a format that complies with the keyboard library standards.

Notes:
- For the script to work correctly, make sure that you do not use these keys in other applications.
- To end the program, you can press the mute key.
'''

import pyautogui as auto
import keyboard as key

start_key = input('Enter the activation button:')
stop_key = input('Enter the off button:')
while True:
    if key.is_pressed(start_key):
        auto.tripleClick()
    if key.is_pressed(stop_key):
        break
