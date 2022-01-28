num=int(input("enter number..."))
num1=int(input("enter number..."))
def add():
    add=num+num1
    return add

def sub():
    sub=num-num1
    return sub

def mul():
    mul=num*num1
    return mul

def div():
    div=num/num1
    return div

def main_fun():
    n=input("enter calculate....")
    if n=='add':
      print(add())
    if n=='sub':
        print(sub())
    if n=='mul':
        print(mul())
    if n=='div':
        print(div())
main_fun()

