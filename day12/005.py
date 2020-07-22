#!/usr/bin/python
## 005. if-elif-else

num1 = 21

if num1 % 3 == 0 and num1 % 7 == 0:
    print(num1, ": 3과 7의 배수")
elif num1 % 3 != 0 :
    print(num1, ": 3의 배수")
elif num1 % 7 == 0 :
    print(num1, ": 7의 배수")
else :
    print(num1, ": 3, 7의 배수가 아님")
