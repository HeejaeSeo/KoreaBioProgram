#!/usr/bin/python
## 034. Count the number of elements with value of a list.

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

d = {}

for x in l :
    if x in d :
        d[x] += 1
    else :
        d[x] = 1

for k, v in d.items() :
    print(f"{k} : {v}")
