#!/usr/bin/env python3

print("Enter a number ")
number = int(input())
multiply = 0
while multiply <= 12:
    result = number * multiply
    print(f"{number} x {multiply} = {result}")
    multiply += 1