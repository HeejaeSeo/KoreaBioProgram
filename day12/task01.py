#!/usr/bin/python

# 2. Print your name
'''
name = input("Enter your name : ")
print(f"NAME : {name}")
print()
'''

# 3. Create a function to print a base
def printBase(base : str) :
    if base == "A" :
        res = "Adenine"
    elif base == "C" :
        res = "Cytosine"
    elif base == "G" :
        res = "Guanine"
    elif base == "T" :
        res = "Thymine"
    elif base == "U" :
        res = "Uracil"
    else :
        print("Wrong base")

    print(f"BASE : {res}")
'''
base = input("Enter a base : ")
printBase(base)
'''


# 4. 10 / n
#num = int(input("Enter a number : "))
num = 3

try :
    res = 10 / num
    print(f"10 / {num} = {res}")

except ZeroDivisionError :
    print(f"You can't divide 10 into 0")


# 5. Factorial
def factorial(n) :
    if n < 2 :
        return n
    else :
        n *= factorial(n - 1)
        return n

res = factorial(5)
print(res)
