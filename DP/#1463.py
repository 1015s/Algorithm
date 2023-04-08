# Dynamic Programming

N = int(input())

num = [0 for i in range(N * 3)]

def divide(N):
    n = 1
   
    while n < N:
        if num[n * 3] == 0 or (num[n] + 1 < num[n * 3]):
            num[n * 3] = num[n] + 1
            
        if num[n * 2] == 0 or (num[n] + 1 < num[n * 2]):
            num[n * 2] = num[n] + 1
        
        if num[n + 1] == 0 or (num[n] + 1 < num[n + 1]):
            num[n + 1] = num[n] + 1 
           
        n += 1
        

divide(N)
print(num[N])

