from math import *
from array import *

n = int(input("enter the number of test cases"))
numar = array('i',[])
denar = array('i',[])
def numconv(a,b):
    x = int(a/b);
    y = int(a%b);
    print("your mixed fraction is = "+ str(x) + " " + str(y) + "/" + str(b))


i = 0
for i in range(n):
    x = int(input("enter the numerator number"))
    y = int(input("enter the denominator number"))
    if x>=0 and x< pow(2,31)-1 and y>=0 and y< pow(2,31)-1 :
        numar.append(x)
        denar.append(y)
    else:
        print("cannot be added")

for i in range(n):
    if(numar[i] == 0 and denar[i] ==0):
        print("your mixed fraction is = 0" + " " + str(numar[i-1]) + "/" + str(denar[i-1]))
    else :
        numconv(numar[i],denar[i])


