#!/usr/bin/env python3

print("Enter the first number:")
first_num = input()
print("Enter the second number:")
second_num = input()
result = int(first_num) * int(second_num)
print(first_num + " x " + second_num + " = " + str(result))
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")