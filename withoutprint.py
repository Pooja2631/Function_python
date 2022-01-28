def evenodd(a):
   i=0
   c=[]
   while i<len(a):
    if a[i]%2==0:
        c.append(a[i])
    i=i+1 
   return c 
b=evenodd([1,2,4,6,8,9,7,5,12]) 
print(b)