# determinant_finder.py
# enter a matrix/determinant to get its value


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
        
det = []

n = int(input("Enter the order of the determinant/square matrix:  "))
for i in range(n):
    det.append(list(map(lambda a: int(a), input().split())))

result = det_exp(det)
print(result)
