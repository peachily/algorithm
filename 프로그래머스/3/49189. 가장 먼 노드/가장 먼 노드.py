from collections import deque

def solution(n, edge):
    graph = {}

    for i in range(1, n+1):
        graph[i] = []

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1]*(n+1)

    q = deque()
    q.append(1)
    distance[1] = 0

    while q:
        start = q.popleft()
        for next in graph[start]:
            if distance[next] == -1:
                q.append(next)
                distance[next] = distance[start] + 1
    
    answer = distance.count(max(distance))

    return answer