#!/usr/bin/python

import sys

class FASTQ :
    def __init__(self, file_name : str) :
        self.file_name = file_name
        self.read_num = 0

    def count_read_num(self) :
        with open(self.file_name, 'r') as handle :
            for line in handle :
            

            

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [fastq]")
        sys.exit()

    file_name = FASTQ(sys.argv[1])
    t = FASTQ(file_name)
    t.count_read_num()

