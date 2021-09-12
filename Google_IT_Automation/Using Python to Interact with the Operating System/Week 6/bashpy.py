'''
In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy. The username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.
What you'll do

    Practice using the cat, grep, and cut commands for file operations
    Use > and >> commands to redirect I/O stream
    Replace a substring using Python
    Run bash commands in Python

student-01-2f1a4f38a09c
'''
#findJane.sh
#!/bin/bash

>oldFiles.txt
 
#grep " jane " ../data/list.txt | cut -d ' ' -f 3 > Files

#while read f ; do
#	if test -e $f; 
#		then echo "File exists"; 
#	else echo "File doesn't exist"; 
#	fi
#; done <Files 

Files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for f in $Files; do 
	if test -e "/home/student-01-2f1a4f38a09c$f";
		then echo "/home/student-01-2f1a4f38a09c$f" >>oldFiles.txt  # tee -a oldFiles.txt
	fi
done

#changeJane.py
#!/usr/bin/env python3

import sys
import subprocess


with open(sys.argv[1],'r') as file:
	lines = file.readlines()
	for line in lines.strip():
		newline = line.replace("jane", "jdoe")
		subprocess.run(['mv',line,newline])
file.close()
