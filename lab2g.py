#!/usr/bin/env python3

# Author: Simranpreet Kaur
# Author ID: 167976216
# Date Created: 2024/06/04

import sys


if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3


while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

