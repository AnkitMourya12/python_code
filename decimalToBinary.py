def calBinary(n):
    if n>1:
        calBinary(n//2)
    print( n%2, end = "")
    
dec=34
calBinary(dec)
print()

        
