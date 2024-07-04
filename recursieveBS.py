def search(arr,l,r,x):
    
    mid=l+(r-l)//2

    if arr[mid]==x:
        return 1
    if arr[mid]<x and l<len(arr):
        l=mid+1
        search(arr,l,r,x)
    if arr[mid]<x and r>0:
        r=mid-1
        search(arr,l,r,x)


    
    # elif mid<x and l<len(arr):
    #     l=mid+1
    #     search(arr,l,r,x)
    # elif mid>x and r>=0:
    #     r=mid-1
    #     search(arr,l,r,x)
    # else:
    #     return -1
    
    return -1

arr = [1,2,3,6,8,9]
x=9

reuslt=search(arr,0,len(arr)-1,x)
if(reuslt!=-1):
    print("number is searched")
else:
    print("not find")

