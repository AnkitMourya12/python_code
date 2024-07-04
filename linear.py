list=[1,2,4,3,5,6]
k=int(input())
for i in range(0,len(list)):
    if k==list[i]:
        print("found at location",i,"-- value",k)
        break