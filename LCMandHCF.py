def cal_lcm(x ,y):
    if x > y:
        g = x
    else:
        g =y
    while(True):
        if g%x==0 and g%y==0:
            lcm=g
            break
        g+=1
        
    # return lcm
    hcf=(x*y)//lcm               

    return hcf
x=24
y=54
print("lcm of",x,"and",y,"is",cal_lcm(x,y))
        
       
