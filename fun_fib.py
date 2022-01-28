def factorical():
    num=int(input("enter your number-----"))
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print("factorical=",fact)
factorical()