# 분할 정복

a, b, c = map(int, input().split())


def power(a, x):
    if x == 1:
        return a % c
    else:
        temp = power(a, x // 2)
        
        if x % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
    
result = power(a, b)

print(result)

    