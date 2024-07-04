c=1
s=7
ff=0
for i in range(1,17):
    if c==1:
        s=s+ff
        c=c+1
        print(s,end=" ")
        continue
    if c%4==0:
        print(c//4,end=" ")
        c=c+1
        continue
        
    s=s+10
    
    print(s,end=" ")
    c=c+1
       
    

        
       
    
       