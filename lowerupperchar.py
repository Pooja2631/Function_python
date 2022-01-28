def upper():
    string='The quick Brow Fox'
    i=0
    co=0
    count1=0
    while i<len(string):
        if string[i].isupper():
            co=co+1
        elif string[i].islower():
            count1=count1+1
        i=i+1
    print(co)
    print(count1)  
upper()
