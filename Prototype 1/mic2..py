from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

time.sleep(2)
with keyboard.pressed(Key.ctrl):
    keyboard.press('d')