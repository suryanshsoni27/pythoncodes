class PyCharm:

    def execute(self):
        print("Complining")
        print('Running')

class  MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()


ide  = PyCharm()

lap1 = Laptop()
lap1.code(ide)


