#!/usr/bin/python

seq1 = "AGTTTATAG"

for i in range(len(seq1)) :
    if seq1[i : i + 2] == "TT" :
        print(i)

print()

for i in range(len(seq1) - 1) :
    if seq1[i : i + 2] == "TT" :    
        print(i, i + 1, seq1[i : i + 2])
