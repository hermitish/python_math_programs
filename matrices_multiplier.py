# matrices_multiplier.py
# multiply two matrices

def mat_mul(mat1, mat2):
    mat = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for x in range(len(mat2)):
                mat[i][j] += mat1[i][x] * mat2[x][j]
    return mat

n1 = input("Enter order of first matrix(separated by 'X'):   ")
n1s = list(map(lambda a: int(a), n1.split('X')))
mat1 = []
for i in range(n1s[0]):
    s = input()
    l = s.split()
    if len(l) == n1s[1]:
        row = list(map(lambda a: int(a), s.split()))
        mat1.append(row)
        
n2 = input("Enter order of second matrix(separated by 'X'):   ")
n2s = list(map(lambda a: int(a), n2.split('X')))
if n1s[1] != n2s[0]:
    print("No. of columns of first matrix MUST be equal to No. of rows of second matrix.")
else:    
    mat2 = []
    for i in range(n2s[0]):
        s = input()
        l = s.split()
        if len(l) == n2s[1]:
            row = list(map(lambda a: int(a), s.split()))
            mat2.append(row)    
    print(mat_mul(mat1, mat2))
    
