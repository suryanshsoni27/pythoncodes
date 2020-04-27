from math import *
from array import *

print("enter number between 1 and 100")
n = int(input("enter the number of cases of one positive integer"))
x = array('i', [])
y = array('i', [])
z = array('i', [])
i = 0
for i in range(n):
    r = int(input("enter r"))
    e = int(input("enter e"))
    c = int(input("enter c"))
    x.append(r)
    y.append(e)
    z.append(c)

for i in range(n):
    if (y[i] < 0 and x[i] < 0):
        print("do not advertise")
    elif (z[i] != (y[i] - x[i]) and z[i] > 0):
        print("advertise")
    elif (z[i] == (y[i]-x[i])):
        print("does not matter")


e


