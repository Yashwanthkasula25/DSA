from array import array 
# length = int(input("enter length "))
# arr = array('i',[])
# for i in range(length):
#     element = int(input("enter elements: "))
#     arr.append(element)
# print(f"array: {arr}")    


#arr = array('i',[1,2,3,4,5,6,7,8,9])
#arr.remove(4)
#del arr[1]
# arr.append(2)
# arr.insert(11,10)
# print(len(arr))
# for i in range(len(arr)-2):
#     print(arr[i] ,end = ' ')
#print(arr.index(3))    
# arr[3] = 10
# arr.reverse()
# print(arr)
#print(arr[: 4])



import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr1 = np.array([[1,3,4],[5,7,8],[2,6,4]])
# print(arr)
# print(arr1)
# print(np.append(arr,10))
# np.delete(1,2)
# print(arr[:,0])
# print(np.prod(arr))


def create_matrix():
    rows = int(input("enter no of rows: "))
    cols = int(input("enter no of columns: "))
    matrix = []
    print('enter elements row wise ')

    if rows == cols:
        for i in range(rows):
   
            element = list(map(int,input().split()))
            matrix.append(element)
    else:
        print('enter equal no of rows and columns')
   # print(f"the matrix is {matrix}", end = ' ' )  
    print("the matrix is")          
    for i in matrix:
        print(i)
    return matrix , rows , cols


def multiply():
    print('matrix 1')
    m1 , row , col = create_matrix()
    print('matrix 2')
    m2 , roww , coll = create_matrix()
    mul = [[0 for _ in range(row)] for _ in range(coll)]
    for i in range(row):
        for j in range(coll):
            for k in range(roww):
                mul[i][j] =  m1[i][k]*m2[k][j]
    print("prod of the matrices")            
    for element in mul:
        print(element)            
    


def addd():
    print("matrix 1")
    m1 , row ,col = create_matrix()
    print("matrix 2")
    m2 , roww , coll = create_matrix()
    add = []
    rows = len(m1)
    col = len(m1[0])
    for i in range(rows):
        temp = []
        for j in range(col):
            temp.append(m1[i][j] + m2[i][j])
        add.append(temp)
    print("addition of the matrices")
    for a in add:
        print(a)        
         


def subtract():
    print("matrix 1")
    m1 , row , col = create_matrix()
    print("matrix 2")
    m2 , roww , coll = create_matrix()
    Row = len(m1)
    Col = len(m1[0])
    sub = []
    for i in range(Row):
        temp = []
        for j in range(Col):
            temp.append(m1[i][j] - m2[i][j])
        sub.append(temp)
    print('subtraction of the matrices')
    for i in sub:
        print(i)        



def transpose():
    print("matrix")
    m , row , col = create_matrix()
    trans = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            trans[j][i] = m[i][j]
    print("transpose of the matrix")
    for i in trans:
        print(i)        



def switch():
    print("1. create matrix 2. multiply matrix 3. add matrix 4. subtract matrix 5. transpose matrix")
    method = int(input("enter option: "))
    if method == 1:
        create_matrix()
    elif method == 2:
        multiply()
    elif method == 3:
        addd()
    elif method == 4:
        subtract()
    elif method == 5:
        transpose()
    else:
        print("option not found enter correct option")
        exit

switch()                        