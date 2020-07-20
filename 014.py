#!/usr/bin/python
## 014. input2

string = input("Enter : ")

if string.isnumeric() :
    print(f"\"{string}\" is number")
elif string.isalpha() :
    print(f"\"{string}\" is string")
else :
    print(f"\n{string}\" is ???")
