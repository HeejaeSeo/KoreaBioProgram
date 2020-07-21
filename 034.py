#!/usr/bin/python

ls = [3, 1, 1, 2, 0, 0, 2, 3, 3] 

# CASE 1
min_val = max_val = ls[0]

for x in ls :
    if x > max_val :
        max_val = x
    if x < min_val :
        min_val = x

print(f"MAX : {max_val}")
print(f"MIN : {min_val}")
print()

# CASE 2
min_val2 = min(ls)
max_val2 = max(ls)

print(f"MAX : {max_val2}")
print(f"MIN : {min_val2}")
