#!/usr/bin/python

import sys

def read_tsv(file_name : str) -> str :
    ret = []

    with open(file_name, 'r') as handle :
        for line in handle :

            if line.startswith("#") :
                header = line.strip().strip("#").split("\t")
                continue

            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
        
    return ret

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [tsv]")

    file_name = sys.argv[1]
    ret = read_tsv(file_name)
    print(ret)

    for line in ret :
        for k, v in line.items() :
            print(f"{k} : {v}")
        print()
