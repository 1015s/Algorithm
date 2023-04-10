# Dynamic Programming

# 계단 수
N = int(input())

# 각 계단의 점수
score = []
score.append(0)

for i in range (N):
    score.append(int(input()))


arr = [0 for i in range(N+1)]
arr[0] = 0
arr[1] = score[1]


def stair(n):
    if n >= 2:
        arr[2] = score[1] + score[2]
    
    if n > 3:
        for k in range (1, n+1):
            temp = arr[k-2] + score[k]
            temp2 = arr[k-3] + score[k-1] + score[k]
            
            arr[k] = max(temp, temp2)


stair(N)
print(arr[N])

        
        
        
        
