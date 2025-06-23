#!/usr/bin/env python3

print("Give me a number: ")
num = float(input())
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")