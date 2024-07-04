lst=[1,2,3,4,5]
n=int(input("enter the no. for rotation:"))
temp=[]
k=len(lst)

j=0
while n>j:
    temp.append(lst[j])
    j=j+1

j=0
while n<k:
    lst[j] = lst[n]
    n=n+1
    j=j+1

lst[:]=lst[:j] + temp    #concatenate
print(lst)



    
