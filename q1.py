list=['aba','xyx','121','345']
def show():
   i=0
   count=0
   while i<len(list):
       j=0
       while j<len(list[i]):
           if list[i][0]==list[i][-1]:
               count=count+1
               print(count,list[i])
               break
           j=j+1
       i=i+1
show()
