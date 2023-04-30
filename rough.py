import math
deg  = lambda x : (x*math.pi/180)
def matrixMultiply(m1,m2):
    matA  = m1
    matB  = m2
    row1,col1,row2,col2 = len(matA),len(matA[0]),len(matB),len(matB[0])
    if col1!=row2:
        print("multiplication not possible🙂🙂")
        return
    res = [[None for i in range(col2)] for j in range(row1)] 
    for i in range(row1):
        for j in range(col2):
            value = 0
            for k in range(row2):
                value += m1[i][k] * m2[k][j]
            res[i][j] = value
    return res
def combined(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        mat = arr[i]
        res = matrixMultiply(res,mat)
    return res
# matA =[
#     [4,6 ,1],
#     [2,2 ,1],
#     [6,2 ,1],
# ]
# TR =[
#     [1,0,0],
#     [0,1,0],
#     [-4,-6,1]
# ]
# ROT = [
#     [math.cos(deg(180)) , math.sin(deg(180)) ,  0],
#     [-math.sin(deg(180)), math.cos(deg(180)) , 0],
#     [0             ,                 0       , 1]
# ]
# TRI =[
#     [1,0,0],
#     [0,1,0],
#     [4,6,1]
# ]
matA =[
    [-1,0 ,1],
    [0,-2,1],
    [1 ,0 ,1],
    [0 ,2 ,1],
]
TR =[
    [1,0,0],
    [0,1,0],
    [2,-4,1]
]
ROT =[
    [1/math.sqrt(5),2/math.sqrt(5),0],
    [-2/math.sqrt(5),1/math.sqrt(5),0],
    [0,0,1]
]
REF = [
    [-1,0 ,0],
    [0,1,0],
    [0,0 ,1]
]
ROTI =[
    [1/math.sqrt(5),-2/math.sqrt(5),0],
    [2/math.sqrt(5),1/math.sqrt(5),0],
    [0,0,1]
]
TRI =[
    [1,0,0],
    [0,1,0],
    [-2,4,1]
]
SCALE=[
    [1.5,0 ,0],
    [0,0.5 ,0],
    [0,0 ,1]
]
# l = [matA,TR,ROT,TRI]

l = [matA,TR,ROT,REF,ROTI,TRI]
# res = matrixMultiply(matA,matB)
res = combined(l)
for i in res:
    print(i)
"""
[(0,0), (0,1), (0,2)], [(0,0), (0,1), (0,2)]
[(1,0), (1,1), (1,2)], [(1,0), (1,1), (1,2)]
[(2,0), (2,1), (2,2)], [(2,0), (2,1), (2,2)]
"""
# print(math.sin(deg(90)))
# 12 8
# 4 8
# -12 -8
# 12 8
# 96 - 32 + -32 +96 + -96 +96