list=[8,6,4,8,4,50,2,7]
def number():
    index=0
    min=list[0]
    while index<len(list):
        if list[index]<min:
            min=list[index]
        index=index+1
    print(min)
number()

list=[1,2,45,6,5,32]
index=0
min=list[0]
while index<len(list):
    j=0
    sec=0
    while j<len(list):
        if list[index]==list[j]<min:
            min=list[index]
        index=index+1    
    print(min)