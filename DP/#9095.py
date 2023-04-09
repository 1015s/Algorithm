# Dynamic Programming
# 마지막에 올 수 있는 수에 따라 나누어 계산 N-1, N-2, N-3

# 테스트 케이스의 개수
N = int(input())

# 테스트 케이스 입력
test = []

for i in range (N):
    test.append(int(input()))


arr = [0 for i in range(12)]
arr[1] = 1
arr[2] = 2
arr[3] = 4

# n을 1, 2, 3의 합으로 나타내는 방법의 수
def addition(n):
    k = 4
    
    if n > 3 :
        while k <= n:
            if arr[k] == 0:
                arr[k] = arr[k-1] + arr[k-2] + arr[k-3]
            k += 1
    


# 결과 출력
for j in range (N):
    addition(test[j])
    print(arr[test[j]])


