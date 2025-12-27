from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

teleport = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

distance = [-1] * (N+1)
q = deque([S])
distance[S] = 0

while q:
    start = q.popleft()

    for nxt in (start-1, start+1):
        if 1 <= nxt <= N and distance[nxt] == -1:
            distance[nxt] = distance[start] + 1
            q.append(nxt)

    for nxt in teleport[start]:
        if distance[nxt] == -1:
            distance[nxt] = distance[start] + 1
            q.append(nxt)

    teleport[start].clear()

print(distance[E])
