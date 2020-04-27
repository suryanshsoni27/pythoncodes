#most likely putcomes of dice
from array import *
from scipy import stats
try:
    n = int(input("enter the first face"))
    m = int(input("enter the second face"))

    i = 1
    j = 1
    a  = array('i',[])
    while i < m:
        while j < n:
            x = i+j
            a.append(x)
            j += 1
        i += 1

    while i < m:
        while j < n:
         print(a[j], end = "")
         j += 1
        print()
        i +=1


    x = stats.mode(a)

    print(x)
    maxx = a[0]/(n*m)

    for i in range(len(a)):
        if(a[i]/n*m > maxx):
            maxx = (a[i]/n*m)


    print(maxx)









except Exception as e:
    print("something went wrong")

finally:
    print("bye the code is done")
