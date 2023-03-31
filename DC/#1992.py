# 분할 정복
# 1780번이랑 완전 비슷하다 !

N = int(input())

arr = []

for i in range (N):
    arr.append(list(map(int, str(input()))))
    

def divide(row, col, n):
    num = arr[row][col]
    
    for i in range (row, row+n):
        for j in range (col, col+n):
            if arr[i][j] != num:
                # divide
                new = n // 2
                
                sub = ['(']
                
                for k in range (2):
                    for l in range (2):
                        sub.append(divide(row + k * new, col + l * new, new))
                
                sub.append(')')
                total = ''.join(map(str, sub))
                return total
    

    return num


result = divide(0, 0, N)

print(result)
            
            
