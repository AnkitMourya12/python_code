def calBinary(n):
    if n>1:
        calBinary(n//8)
    print( n%8, end = "")
    # calBinary(n//16)            conversion in hexdecimal
    # print( n%8, end = "")
    
dec=34
calBinary(dec)
print()

        
