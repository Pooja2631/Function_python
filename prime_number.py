def primeornot():
    i=0
    co=0
    num=int(input("enter the number...."))
    while i<=num:
        co=co+1
        if num%3==0:
            print("its prime number")
        else:
            print("its not prime number")
            i=i+1
        break
primeornot()