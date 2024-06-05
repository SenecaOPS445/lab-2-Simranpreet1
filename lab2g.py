#!/usr/bin/env python3

# Author: Simranpreet Kaur
# Author ID: 167976216
# Date Created: 2024/06/04

import sys

# Check if an argument was provided and set the timer accordingly
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

# Loop to count down and print the timer
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

