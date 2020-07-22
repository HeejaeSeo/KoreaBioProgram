#!/usr/bin/python
## p3_kmerGeneration

import sys

l1 = l2 = ['A', 'C', 'G', 'T']

def mer(l1 : list, l2 : list, n : int) :
    if n == 1 :
        return l2

    ltmp = []

    for s1 in l1 :
        for s2 in l2 :
            ltmp.append(s1 + s2)
    return mer(l1, ltmp, n - 1)

k = int(sys.argv[1])
res = mer(l1, l2, k)

print(res)

'''
for x in res :
    print(x)
'''
