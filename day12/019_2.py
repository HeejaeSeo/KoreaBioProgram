#!/usr/bin/python
## 019_2. Debugging2

import sys

if len(sys.argv) != 2 :
    print(f"# usage : python {sys.argv[0]} [num]")
    sys.exit()

try :
    num = int(sys.argv[1])
    print(10 / num)

except ValueError :
    print("Input is not valid")
    sys.exit()

except ZeroDivisionError :
    print(f"===== Cannot divide into 0 =====")
