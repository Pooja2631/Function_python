list=[8,-5,22,-3]
def number():
  i=0
  max=0
  while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
  print(max) 
number()   
   