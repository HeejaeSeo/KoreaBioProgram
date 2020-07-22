#!/usr/bin/python

import sys
import json

# 4. 

def read_csv(file_name : str) -> list :
    ret = []
    with open(file_name, 'r') as handle :
        for line in handle :
            if line.startswith("sample") :
                header = line.strip().split(",")
                continue

            line = line.strip().split(",")
            d = dict(zip(header, line))
            ret.append(d)
    return ret

def write_json(l : list, file_name : str) :
    with open(file_name, 'w') as handle :
        json.dump(l, handle, indent = 4)

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [csv]")
        sys.exit()

file_name = sys.argv[1]
ret = read_csv(file_name)
write_json(ret, "task_result.json")


# 5.
seq = "ATAGCGCAGTC"

k = int(input("Enter the number : "))

for i in range(len(seq) - k + 1) :
    print(seq[i : i + k])
print()


# 6.
seq = "ATAGATATATCGCAGTC"
d = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'C'}

# Create 7mer
for i in range(len(seq) - 7 + 1) :
    tmp_seq = seq[i : i + 7]
    flag = 0

    for i in range(4) :
        if tmp_seq[i] != tmp_seq[-(i + 1)] :
            flag = 1

    if flag == 0 :
        print(f"{tmp_seq} is palindrome")
    else :
        print(f"{tmp_seq} is not palindrome")
