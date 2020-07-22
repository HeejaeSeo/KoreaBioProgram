#!/usr/bin/python

cnt_alt = 0

with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("##") :
            continue
        elif line.startswith("#") :
            header = line.strip().split("\t")
            alt_idx = header.index("ALT")
            continue

        line = line.strip().split("\t")
        
        if "," in line[alt_idx] :
            cnt_alt += line[alt_idx].count(",") + 1
        else :
            cnt_alt += 1

print(f"ALT : {cnt_alt}")
