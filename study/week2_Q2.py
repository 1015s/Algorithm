# 다익스트라

import heapq
INF = int(1e9)

def solution(n, paths, gates, summits):
    answer = []

    summits.sort()
    summits_set = set(summits)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    pq = []
    distance = [INF] * (n + 1)

    for gate in gates:
        heapq.heappush(pq, (0, gate))
        distance[gate] = 0

    while pq:
        intensity, now = heapq.heappop(pq)

        if now in summits_set or intensity > distance[now]:
            continue

        for next, cost in graph[now]:
            new_intensity = max(intensity, cost)
            if new_intensity < distance[next]:
                distance[next] = new_intensity
                heapq.heappush(pq, (new_intensity, next))

    for summit in summits_set:
        answer.append([summit, distance[summit]])
    
    # intensity 동일할 경우 summit# 작은 것 선택
    answer.sort(key=lambda x:x[0])
    return min(answer, key=lambda x: x[1])