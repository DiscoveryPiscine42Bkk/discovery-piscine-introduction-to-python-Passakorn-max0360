#!/usr/bin/env python3

arr_num = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
seen = set()
for x in arr_num:
    if x > 5 and x not in seen:
        new_arr.append(x+2)
        seen.add(x)
print(arr_num, "$")
print("{" + ", ".join(str(x) for x in new_arr) + "}$")
