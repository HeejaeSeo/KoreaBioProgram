#!/usr/bin/python

seq1 = "ATGTTATAG"

for i in range(0, len(seq1), 3) :
    print(f"{i + 1} : {seq1[i]}")


