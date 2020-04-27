from array import *

a = array('i',[])

for i in range(8):
    x = int(input("enter = "))
    a.append(x)


for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1] :
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    print(a)