# def show(n):
#     a=0
#     b=1
#     c=0
#     while c<=n:
#         print(c)
#         a=b
#         b=c
#         c=a+b
# n=int(input("enter number...."))
# show(n)

# def compare_lists():
#     llist1=[1,2,3]
#     llist2=[1,2,3,4]
#     i=0
#     while i<len(llist1):
#         if llist1==llist2:
#             return 1
#         elif llist1!=llist2:
#             return 0
#     i=i+1
# print(compare_lists())

# n=int(input("enter the number.."))
# x=0
# y=1
# z=0
# while (z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# n=int(input("enter number..."))
# i=1
# while i<=n:
#     print(i,end="")
#     i=i+1

# def show():
#     a=int(input("enter number..."))
#     if a>0:
#         return a
#     else:
#         return -a
# print(show())   

# def swap_case(s):
#     s1=s.swapcase()
#     return s1
# print(swap_case("deepti_POOJA"))

# n=int(input("enter number..."))
# i=0
# while i<=n:
#     print(i*i)
#     i=i+1

# n= int(input("enter your number...."))
# if  n%2!=0:
#     print("weird")
# elif n>=2 and n<=5:
#     print("ot weird")  
#     print("weird")    
# elif n>=6 and n<=20:
#     print("not weird") 
# elif n>=20:     

n=int(input("enter num...."))
i=1
a=[]
while i<=n:
    name1=input("enter any name....")
    num=int(input("enter any number...."))
    j=1
    li=[]
    while j<=1:
        li.append(name1)
        li.append(num)
        print(li)
        j=j+1
    a.append(li)
    i=i+1
print(a)

# name=input("enter any name....")
# str=""
# i=0
# while i<len(name):
#     if name[i]=='a'or name[i]=='e'or name[i]=='i'or name[i]=='o'or name[i]=='u':
#        pass
#     else:
#         str=str+name[i]
#     i=i+1
# print(str)
