# 분할 정복
# print('\n') 쓰면 안되는건가 ..? 출력 형식 때매 틀렸었음

N = int(input())

arr = [['']* N for i in range(N)]


def pattern(row, col):
    for i in range (3):
        for j in range (3):
            arr[row+i][col+j] = '*'
    
    arr[row+1][col+1] = ' '
    
   
    

def star(row, col, n):
    if n == 3:
       pattern(row, col)
    else:
        # divide
        new = n // 3
        
        for i in range (3):
            for j in range (3):
                star(row + i * new, col + j * new, new)
                
                if i == 1 and j == 1:
                    for k in range (row + new, row + 2 * new):
                        for l in range (col + new, col + 2 * new):
                            # 공백 만들기
                            arr[k][l] = ' '
                        
                        
        
        

star(0, 0, N)


for row in range (N):
    for col in range (N) :
        print(arr[row][col], end='')
        
        if col == N-1 and row != N-1:
            print()
 