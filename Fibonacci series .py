def show(n):
    a=0
    b=1
    c=0
    while c<=n:
        print(c)
        a=b
        b=c
        c=a+b
n=int(input("enter no...."))
show(n)