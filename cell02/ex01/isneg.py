#!/usr/bin/env python3

input_num = input()
if input_num < "0":
    print("This number is negative.")
elif input_num > "0":
    print("This number is positive.")
elif input_num == "0":
    print("This number is both positive and negative.")