#!/usr/bin/python

import sys

# CASE 01. For
l_fibo = [0, 1]
n1 = 0
n2 = 1

#num = int(input("Enter the number : "))
num = 7

if num < 2 :
    res = l_fibo[num]

else :
    for i in range(num - 2) :
        tmp = l_fibo[-1] + l_fibo[-2]
        l_fibo.append(tmp)

    print(l_fibo[num - 1])

#print(f"l_fibo : {l_fibo}")


# CASE 02. Recursive Function
def fib(n : int) -> int :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n - 1) + fib(n - 2)

n = int(sys.argv[1])

print(fib(n))
