#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt

cnt_snp = cnt_ins = cnt_del = 0
d_cnt = {'snp' : 0, 'ins' : 0, 'del' : 0}

with open("070.vcf", 'r') as handle :
    for line in handle :
        if line.startswith("##") :
            continue
        elif line.startswith("#") :
            header = line.strip().split("\t")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue
        line = line.strip().split("\t")
        
        l_alt = line[alt_idx].split(",")
        ref = line[ref_idx]

        for alt in l_alt :
            if len(ref) == len(alt) :
                d_cnt["snp"] += 1
            elif len(ref) > len(alt) :
                d_cnt["del"] += 1
            elif len(ref) < len(alt) :
                d_cnt["ins"] += 1
            else :
                raise   # raise Error

for k, v in d_cnt.items() :
    print(f"{k} : {v}")

df = pd.DataFrame([d_cnt])
df.plot.bar()
plt.savefig("snp.png")
