#!/usr/bin/python

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as handle :
    for line in handle :
        ch, start, end  = line.strip().split("\t")
        read_len = int(end) - int(start)
        print(f"{chr} : {read_len}")
