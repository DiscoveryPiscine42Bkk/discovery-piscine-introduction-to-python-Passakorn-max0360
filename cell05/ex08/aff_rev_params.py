#!/usr/bin/env python3

import sys
mem = len(sys.argv) - 1
if mem >= 2:
    while mem >= 1: 
        print(sys.argv[mem] + "$")
        mem -= 1 
else:
    print("none$")
