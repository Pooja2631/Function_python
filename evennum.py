a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def evenodd():
    i=0
    c=[]
    while i<len(a):
        if a[i]%2==0:
            c.append(a[i])
        i=i+1 
    return(c)
print(evenodd())


