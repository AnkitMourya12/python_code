
def matrix(a,b):
    mat=[]
    for i in range(a):
        row=[]
        for j in range(b):
            val=int(input("enter the no."))
            row.append(val)
        mat.append(row)
    return mat

# def matrix1(a,b):
#     mat1=[]
#     for i in range(a):
#         row1=[]
#         for j in range(b):
#             val1=int(input("enter the no"))
#             row1.append(val1)
#         mat1.append(row1)
#     return mat1

def add(m1,m2):
    ans=[]
    for i in range(len(m1)):
        row2=[]
        for j in range(len(m1[0])):
            val2=int(m1[i][j]+m2[i][j])
            row2.append(val2)
        ans.append(row2)
    return ans

a=int(input("enetr the row"))
b=int(input("enetr the coloumn"))
m1=matrix(a,b)
print(m1, end=" ")
print()
m2=matrix(a,b)
print(m2, end=" ")
print()
s=add(m1,m2)
print(s)


