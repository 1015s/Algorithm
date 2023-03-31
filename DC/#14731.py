# 분할 정복
# RecursionError 뭔가 했는데 python은 기본 depth가 1000밖에 안된다..

import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

m = pow(10, 9) + 7


def fast_power(num, x):
    if x == 0:
        return 1
    else:
        temp = fast_power(num, x // 2) % m
        
        if x % 2 == 0:
            return (temp * temp) % m
        else:
            return (temp * temp * num) % m



result = 0

for _ in range (int(input())):
    C, K = map(int, input().split())
    
    if K > 0:
        result += C * K * fast_power(2, K-1)

print(result % m)
    
    
