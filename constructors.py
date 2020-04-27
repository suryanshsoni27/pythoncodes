class Computer:

    def __init__(self):
        self.age = 28
        self.name = "sun"



    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
c1.age = 12
print(c1.name)
print(c2.name)
