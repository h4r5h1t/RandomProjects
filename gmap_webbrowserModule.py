#! python3

import webbrowser, sys, pyperclip


if len(sys.argv) > 1 : 
    address = ' '.join(sys.argv[1:])
else: 
    adress = pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/place{address}")
