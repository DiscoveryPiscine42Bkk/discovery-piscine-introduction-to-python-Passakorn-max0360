#!/usr/bin/env python3

number = int(input())
if number > 25:
    print("Error")
else:
    while number <= 25:
          print(f"Inside the loop, my variable is "+ str(number))
          number += 1