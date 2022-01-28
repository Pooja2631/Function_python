def palidrom(s):
    if (s==s[::-1]):
       return ("its is palidrom")
    else:
       return ("its is not palidrom")
s=input("enter a string....")
d=palidrom(s)
print(d)