age=int(input("enter the number....."))
def age_check():
    if age<14:
        print(" Kids drink toddy")
    if age>14 and age<18:
        print("Teens drink coke")
    if age>18 and age<21:
        print("Young adults drink beer")
    if age>21:
        print("Adults drink whisky")
    else:
        ("pass")
age_check()
        