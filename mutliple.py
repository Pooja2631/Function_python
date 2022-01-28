list= (8, 2, 3, -1, 7)
def num():
    i=0
    mul=1
    while i<len(list):
        mul=mul*list[i]
        i=i+1
    print(mul)
num()