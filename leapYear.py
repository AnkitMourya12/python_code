year=int(input("enter the year: "))
if (year%400==0 or year%4==0):
    print('it is leap year')
else:
    print('not a leap year')
