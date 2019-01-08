row,col=input("enter no of rows and cols of a matrix : ").split()
row=int(row)
col=int(col)
matrix_1=[]
for i in range(row):
    row_list=[ ]
    for j in range(col):
        s='input the val of [{0}] [{1}] is :'.format(i,j)
        ele=input(s)
        row_list.append(ele)
    matrix_1.append(row_list)
for i in range(row):
    print()
    for j in range(col):
        print(matrix_1[i][j],end=' ')
print("\n")
print(matrix_1)
