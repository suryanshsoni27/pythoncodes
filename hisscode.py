#hiss code

st = input("enter the word:: ")


def hiss(st):
    if st[len(st)-1]== 's' and st[len(st)- 2] == 's' :
        print("hiss")
    else:
        print("no hiss")



hiss(st)