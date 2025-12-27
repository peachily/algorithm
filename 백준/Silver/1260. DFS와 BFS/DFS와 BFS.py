from collections import deque

N, M, V = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, N + 1):
    edges[i].sort()

visited = [False] * (N + 1)
dfs_order = []

stack = [V]

while stack:
    cur = stack.pop()
    if not visited[cur]:
        visited[cur] = True
        dfs_order.append(cur)
        for nxt in reversed(edges[cur]):
            if not visited[nxt]:
                stack.append(nxt)

visited = [False] * (N + 1)
bfs_order = []

q = deque([V])
visited[V] = True

while q:
    cur = q.popleft()
    bfs_order.append(cur)
    for nxt in edges[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

print(*dfs_order)
print(*bfs_order)
