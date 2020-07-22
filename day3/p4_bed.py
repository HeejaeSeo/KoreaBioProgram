#!/usr/bin/python

import sys

file_name = sys.argv[1]
total_len = 0

with open(file_name, 'r') as handle :
    for line in handle :
        start, end  = line.strip().split("\t")[1 : 3]
        total_len += ( int(end) - int(start) ) 

print(f"TOTAL LENGTH : {total_len}")
