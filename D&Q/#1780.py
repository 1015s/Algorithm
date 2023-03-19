# 분할 정복

N = int(input())

arr = []

for i in range (N):
    arr.append(list(map(int, input().split())))

# call by reference 쓰기 위함
result = {-1 : 0, 0 : 0, 1 : 0}



def divide(row, col, n):
    num = arr[row][col]
    
    for i in range (row, row+n):
        for j in range (col, col+n):
            if arr[i][j] != num:
                # 분할 필요    
                line = n // 3
                
                for k in range (3):
                    for l in range (3):
                        divide(row + line * k, col + line * l, line)
                
                return 
    
    result[num] += 1
            
    
    
divide(0, 0, N)

for i in result.values():
    print(i)
