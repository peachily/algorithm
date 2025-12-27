from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n+1)

q = deque()
q.append(1)
visited[1] = 0

count = 0

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = 0
            q.append(i)
            count += 1

print(count)
