#!/usr/bin/env python3

import sys

mem = len(sys.argv) - 1
if mem >= 1:
    print(f"parameters: {mem}$")
    for i in range(1, mem + 1):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}$")
else:
    print("none$")
