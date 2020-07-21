#!/usr/bin/python

import sys
import gzip

if len(sys.argv) != 2 :
    print(f"# usage : python {sys.argv[0]} [fasta.gz]")

f = sys.argv[1]

d = {}
total = 0

with gzip.open(f, 'rb') as handle :
    for line in handle :
        line = line.decode("utf-8").strip()

        if line.startswith(">") :
            continue

        # Count bases
        for base in line :
            if base in d :
                d[base] += 1
            else :
                d[base] = 1

            total += 1

# Write
with open("result1.txt", 'w') as handle :
    handle.write(f"A : {d['A']}\n")
    handle.write(f"C : {d['C']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"T : {d['T']}\n")
    handle.write(f"TOTAL : {total}\n")
