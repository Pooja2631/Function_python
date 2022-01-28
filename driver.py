num=int(input("enter the number...."))
def speed():
    point=1
    co=0
    if num<70:
        print("ok")
    elif num>70:
        b=num-70
        point=b//5
        print("point",point)
        if point>12:
            print("lincense suspended")
    else:
        print("ok")
        co=co+1
speed()
