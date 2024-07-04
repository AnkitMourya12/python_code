def EratosPrim(num):
    prime = [1 for i in range(num+1)]

    p = 2
    while (p * p <= num):
        if (prime[p] == 1):
            for i in range(p * p, num+1, p):
                prime[i] = 0
        p += 1
 
    for p in range(2, num+1):
        if prime[p]==1:
            print(p)
 
num = 5
EratosPrim(num)
   
 
 

        
            
 

