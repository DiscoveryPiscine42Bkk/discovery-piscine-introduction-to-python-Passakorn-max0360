#!/usr/bin/env python3

number = 0
while number <= 10:
    multiply = 0
    print(f"Table de {number}:", end=" ")
    while multiply <= 10:
        result = number * multiply
        print(result, end=" ")
        multiply += 1
    print()  # Move to the next line after each row
    number += 1