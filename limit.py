def limit():
    i=1
    sum=0
    while i<=10:
        if i%3==0:
            print("divisible 3....",i)
            sum=sum+i
        if i%5==0:
            print("divisible 5....",i)
            sum=sum+i
        i=i+1
    print(sum)
limit()