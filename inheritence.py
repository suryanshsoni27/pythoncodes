class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature one")

    def feature2(self):
        print("feature two")

;
class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature(self):
        print("feature one")

    def feature(self):
            print("feature one")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):


a1 = C()


a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()

