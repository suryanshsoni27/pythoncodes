from functools import reduce
from factorial import *


def add_all(a,b):
    return a+b

def is_even(n):
    return n%2==0
nums  = [4,3,2,5]

evens = list(filter(lambda n:n%2==0, nums))
doubles = list(map(lambda n:n+2, evens))

print(evens)
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum)
c = fact(sum)
print(c)


