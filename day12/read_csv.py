#!/usr/bin/python

import sys

def read_csv(file_name : str) -> str :
    ret = []

    with open(file_name, 'r') as handle :
        for line in handle :

            if line.startswith("#") :
                header = line.strip().strip("#").split(",")
                continue

            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
        
    return ret

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [csv]")

    file_name = sys.argv[1]
    ret = read_csv(file_name)
    print(ret)

    for line in ret :
        for k, v in line.items() :
            print(f"{k} : {v}")
        print()
