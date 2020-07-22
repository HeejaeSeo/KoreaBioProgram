#/usr/bin/python
## 007. Multiplication table

for i in range(2, 10, 2) :
    print("===== {} Dan =====".format(i))
    for j in range(1, 10) :
        #print("{} X {} = {}".format(i, j, i * j))
        print(f"{i} X {j} = {i * j}")
    print()

