
def matrix(a,b):
    mat=[]
    for i in range(a):
        row=[]
        for j in range(b):
            val=int(input("enter the no."))
            row.append(val)
        mat.append(row)
    return mat


def product(m1,m2):
    r=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
         
            for k in range(len(m2)):
                r[i][j]=r[i][j]+m1[i][k]*m2[k][j]
    return r

a=int(input("enetr the row :"))
b=int(input("enetr the coloumn :"))
m1=matrix(a,b)
print(m1, end=" ")
print()
print("enter the 2nd matrix")
m2=matrix(a,b)
print(m2, end=" ")
print()
# s=add(m1,m2)
# print(s)
res=product(m1,m2)
print(res)

