
from numpy import *
from array import *
print("hello world")
print("you want candies ?")

av = 100

x = int(input("enter the amount of candies you want"))

i = 1
while i <= x:

    if i>av:
        print("out of stock")
        break

    print("Candy")
    i+=1

print("Bye")







for i in range(1,101):

    if i%3==0 or i%5==0:
        continue

    print(i)

print("Bye")



for i in range(5):

    if i==3:
        break
    print("hello",i)

def fun():
    pass

for j in range(4):
    for i in range(j):
      print('#',end="")
    print()



nums = [12,12,18,21,26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
        print("not found")



num = 7
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break

else:
    print("prime")


vals = array('i',[5,6,56])
vals.reverse()

for i in range(len(vals)):
    print(vals[i])

vals = array('i',[5,4,4,-9,2])

newArr = array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)

i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1


n = int(input("enter the length of the array"))
arr = array('i',[])
for i in range(n):
    x  = int(input("input the value "))
    arr.append(x)

print(arr)

val = int(input("enter the value for search"))

k = 0
for e in arr:
    if e==val:
       print(k)
       break
    k = k+1
print(arr.index(val))




arr = array([1,2,3],[2,5,4])
print(arr)














