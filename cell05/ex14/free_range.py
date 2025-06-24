#!/usr/bin/env python3

import sys

if len(sys.argv)-1 != 2:
    print("none$")
else:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    arr = list(range(first, second + 1))
    print(f"{arr}$")    

