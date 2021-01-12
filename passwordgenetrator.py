#!/usr/bin/env python

# modules
import random

# declaring variables
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()_+=-*&^%$#@!~`:|?.,{}[]/"

# setting boolean values
uppercase, lowercase, number, symbol = True, True, True, True,

all = ""

# setting password gen conditions
if uppercase:
    all += uppercase_letters
if lowercase:
    all += lowercase_letters
if number:
    all += digits
if symbol:
    all += symbols

# lenght and amount of passwords we get
length = 20
amount = 10

'''
To generate the same password use
seed = "gizmo" 
random.seed(seed)
'''

# generating passwords
for x in range(amount):
    password = "".join(random.sample(all, length))
    print("Your password: " + password)
