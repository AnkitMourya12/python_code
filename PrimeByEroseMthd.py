def erosePrime(n):
    masterList=[i for i in range(1,n+1)]
    for i in range(2,n):
        for j in range(i*2,n+1,i):
            if j%i==0 and i in masterList:
                del masterList[j]
                      
        return masterList







num=30
stor=erosePrime(num)
print(stor)


