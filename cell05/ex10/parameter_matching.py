#!/usr/bin/env python3

import sys

mem = len(sys.argv) - 1
if mem == 1:
    answer = input("What was the parameter? ")
    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
