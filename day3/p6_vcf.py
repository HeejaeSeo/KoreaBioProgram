#!/usr/bin/python

import sys

file_name = sys.argv[1]

class VCF :
    def __init__(self, file_name : str) :
        self.file_name = file_name
        self.header = []
        self.data = []
        self.line_num = 0

    def read_vcf(self) :
        with open(file_name, 'r') as handle :
            for line in handle :
                if line.startswith("##") :
                    continue
                elif line.startswith("#") :
                    self.header = line.strip().split("\t")
                else :
                    self.data.append(line.strip())

    def read_line(self) :
        pass

    def filter_pass(self) :
        pass_num = 0
        with open(file_name, 'r') as handle :
            for line in handle :
                if line.startswith("#") :
                    continue
                splitted = line.strip().split("\t")
                if splitted[5] == "PASS" :
                    pass_num += 1
        return pass_num

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"# usage : python {sys.argv[0]} [vcf]")
        sys.exit()

    file_name = sys.argv[1]
    a = VCF(file_name) 
    a.read_line()
    print(a.line_num)
    print()
    
    pass_num = a.filter_pass()
    print(f"PASS NUM : {pass_num}\n")
