#!/usr/bin/python

import sys

def comp1(seq) :
    comp =  ""
    for s in seq :
        if s == "A" :
            comp += "T"
        elif s == "C" :
            comp += "G"
        elif s == "G" :
            comp += "C"
        elif s == "T" :
            comp += "A"
    return comp

def comp2(seq) :
    d = {'A' : 'T' , 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    comp = ""
    for s in seq :
        comp += d[s]
    return comp

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("# usage : python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]
    
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)

