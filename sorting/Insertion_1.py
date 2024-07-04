def insertion(data):
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while(j>=0 and data[j]>key):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
    return data


data=[13,4,65,36,7,8]
ans=insertion(data)
print(ans)
