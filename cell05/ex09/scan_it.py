#!/usr/bin/env python3

import re
import sys

mem = len(sys.argv) - 1
if mem == 2:
    match = re.findall(sys.argv[1], sys.argv[2])
    if match:
        print(f"{len(match)}$")
    else:
        print("none$")
else:
    print("none$")
