n=6543274546957100
ans=n
i=0
while n!=0:
    n=n//10
    i=i+1
print("Total count Of digit in Given no.:",i)
ff=i-1
while(i>0):
    rem=abs(ans%10**i)
    print(rem,end=" ")      
    ans=ans%10**i
    i=i-1



 