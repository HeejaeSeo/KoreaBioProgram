#!/usr/bin/python

import sys

file_name = ("070.vcf")

with open(file_name, 'r') as handle :
    for line in handle :
        if line.startswith("##") :
            continue

        elif line.startswith("#") :
            header = line.strip().split("\t")
            chr_idx = header.index("#CHROM")
            pos_idx = header.index("POS")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            id_idx = header.index("ID")

        line = line.strip().split("\t")

        if line[2] != "." :
            print(f"{line[chr_idx]}\t{line[pos_idx]}\t{line[ref_idx]}\t{line[alt_idx]}\t{line[id_idx]}")
