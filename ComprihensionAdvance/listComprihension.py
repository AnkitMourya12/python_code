# import random
# list=[random.randint(10,100) for i in range(20)]
# print(list)

# O/P= [76, 22, 71, 23, 86, 96, 31, 34, 96, 72, 62, 29, 69, 43, 26, 80, 45, 18, 19, 81]


# list1=["aam","kela","angoor","amrood","cheeku"]
# list=[x for x in list1 if "a" in x]
# print(list)

# O/P=['aam', 'kela', 'angoor', 'amrood']


# a=20;
# v=0
# c=a//v
# print(c)

# error--> ZeroDivisionError: integer division or modulo by zero


# b=10000
# if b>2999
#     print("you eligible")

#     error--> SyntaxError: expected ':'

try:
    a=20
    b=0
    c=a//b
    print(c)

except:
    print("can' divide with zero")
