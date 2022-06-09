#!/usr/bin/env python

import time
import threading
from pynput.mouse import Button, Controller, Listener

button = Button.left
mouse = Controller()

def on_scroll(x, y, dx, dy):
	if dy != 0:
		mouse.click(button)

with Listener(on_scroll=on_scroll) as listener:
    listener.join()
