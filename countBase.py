#!/usr/bin/python

import sys

def countbase(file_name : str) -> str :
    d = {}

    with open(file_name, 'r') as handle :
        for line in handle :
            if line.startswith(">") :
                continue

                if seq in d :
                    d[seq] += 1
                else :
                    d[seq] = 1
    return d


if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [fasta]")

    file_name = sys.argv[1]
    d_cnt = countbase(file_name)

    for k, v in d_cnt.items() :
        print(f"{k} : {v}")
