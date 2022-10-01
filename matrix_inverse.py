# matrix_inverse.py
# get inverse of a matrix

def adjoint(mat):
    adj = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            # adj[j][i] = cofactor[i][j] = (-1) ** (i + j) * det_exp(new_mat)
            new_mat = [[0] * (len(mat) - 1) for _ in range(len(mat) - 1)]
            a = 0
            b = 0
            for x in range(len(mat)):
                if x != i:
                    for y in range(len(mat)):
                        if y != j:
                            print(a, b)
                            print(x, y)
                            print()
                            new_mat[a][b] = mat[x][y]
                            b += 1
                    a += 1
            adj[i][j] = (-1) ** (i + j) * det_exp(new_mat)
    return adj

def det_exp(det):
    result = 0
    order = len(det)
    if order == 1:
        return det[0][0]    
    for j in range(len(det[0])):
        det_new = []
        for y in range(1, len(det)):
            temp = []
            for x in range(len(det[0])):
                if x != j:
                    temp.append(det[y][x])
            det_new.append(temp)
        result += ((-1) ** j) * det[0][j] * det_exp(det_new)
    return result

def inverse(mat):
    adj = adjoint(mat)
    det_result = det_exp(mat)
    for i in range(len(adj)):
        for j in range(len(adj)):
            adj[i][j] /= det_result
    return adj

n = int(input("Enter order of square matrix:   "))
mat = []
for i in range(n):    
    mat.append(list(map(lambda a: int(a), input().split())))
print(inverse(mat))
