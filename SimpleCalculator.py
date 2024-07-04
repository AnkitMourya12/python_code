def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b


print("*******************************************SIMPLE CALCULATOR*******************************************")
print("                                         ENTER THE TWO NO FOR CALCULATION                              ")   
a=int(input("                                           ENTER THE  NO first "))
b=int(input("                                           ENTER THE NO second "))

print("*******************************************choose  Operation*******************************************")

print("*                                           ADD for press 1:                                          *")
print("*                                           Subtraction for press 2:                                  *") 
print("*                                           Multiplication for press 3:                               *")
print("*                                           Division for press 4:                                     *")

t=int(input("                                            operation no. "))


if t==1:
    print("                                           Add",add(a,b))
if t==2:
    print("                                           subtract is",sub(a,b))
if t==3:
    print("                                           multiply",mul(a,b))
if t==4:
    print("                                           division",div(a,b))
if t>4:
    print("*******************************************Invalid operation*******************************************")
    

    

 
