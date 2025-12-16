from collections import deque

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(input())

distance = [[-1] * M for _ in range(N)]

q = deque()
q.append((0,0))
distance[0][0] = 0

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x = q.popleft()
    for di in range(4):
        dy, dx = dir[di]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == "1" and distance[ny][nx] == -1:
            distance[ny][nx] = distance[y][x] + 1
            q.append((ny, nx))

print(distance[N-1][M-1] + 1)