# n_pascal.py
# prints first 'n' rows of Pascal's Triangle

def n_pascal(n):
    prev_row = [1]
    print(1)
    for i in range(1, n):
        row = [-1] * (i + 1)
        row[0] = prev_row[0]
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        row[-1] = prev_row[-1]
        prev_row = row
        for x in row:
            print(x, end=' ')
        print()

try:
    n = int(input("Enter number of rows: "))
    if n >= 1:    
        n_pascal(n)
    else:
        print("Enter a valid value for 'n'")
except:
    print("Enter a valid value for 'n'")
