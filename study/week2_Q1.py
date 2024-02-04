INF = int(1e9)

def solution(n, s, a, b, fares):
    distance = distance_graph(n,fares)
    array= []
    for k in range (1,n+1):
        array.append(distance[s][k] + distance[k][a] + distance[k][b])
    answer = min(array)
    return answer

# 최단거리 배열 만들기
def distance_graph(n, fares):
    distance = [[INF] * (n+1) for _ in range(n+1)]

    for a in range (1, n+1):
        for b in range (1, n+1):
            if a == b:
                distance[a][b] = 0
    
    for fare in fares:
        distance[fare[0]][fare[1]] = fare[2]
        distance[fare[1]][fare[0]] = fare[2]

    for k in range (1, n+1):
        for a in range (1, n+1):
            for b in range (1, n+1):
                distance[a][b] = min(distance[a][k] + distance[k][b], distance[a][b])

    return distance
