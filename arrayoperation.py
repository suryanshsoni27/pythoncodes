from numpy import *
arr = array([1,2,5,66,8,9,0],int)
print(arr)

arrr = array([1,3,4,5.0],float)

print(arr.dtype)
print(arrr)

ar1 = linspace(0,16,20)
print(ar1)

arr4 = arange(1,15,2)
print(arr4)

arrn = logspace(1,40,5)
print('%.2f%',arrn[4])

arr45 = zeros(5,int)
print(arr45)


a = array([1,4,5,3,4,3])
b = array([1,4,2,5,6,4])
a = a + 5

c = a + b
print(sin(a))

print(c)



f  = array([23,232,32,32,32])
d = f
print(f)
print(d)
f[1] = 5
print(id(f))
print(id(d))


arew = array( [
       [1,2,4,5],
       [4,5,3,6]
              ])

arr2 = arew.flatten()
arr3 = arr2.reshape(2,4)

print(arew)
print(arr2)
print(arr3)

m1 = matrix('1 3 4 ; 5 4 3 ; 3 5 3')
m2 = matrix('1 3 5; 5 6 4; 2 32 2')

m3 = m2 * m1

print(m)
print(diagonal(m))
print(m.max())

print(m3)


