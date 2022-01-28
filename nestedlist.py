list="i am pooja"
def spilt():
    i=0
    a=[]
    string=""
    while i<len(list):
        string=string+str(list[i])
        a.append([i])
        i=i+1
    print(a)
spilt()


