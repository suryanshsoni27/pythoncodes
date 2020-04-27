def great ():
    print("helo")
    print("good")

great()

def add(x,y):
    c = x+y
    return c
    print(c)

add(5,8)
result = add(5,4)

def update(x):


    x = 8
    print(x)


a = 10
print(id(a))
update(a)
print(a)
print("a",a)
lst = [10,20,30]
print(id(lst))
update(lst)
print("lst", lst)

def add(a,b):
    c = a+b


add(7,9)



def person(name, **data):
    print(name)
    print(data)



person('suryansh',age = 28,city= 'delhi',mob = 122121)


