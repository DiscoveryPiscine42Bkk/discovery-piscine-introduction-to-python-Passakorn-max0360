#!/usr/bin/env python3

password = "Python is awesome"
entered_password = input()
if entered_password == password:
    print("ACCESS GRANTED")
if entered_password != password:
    print("ACCESS DENIED.")