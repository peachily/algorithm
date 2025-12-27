from collections import deque

# 1. 격자 크기
N, M = 5, 5

# 2. 방문 배열과 거리 배열 초기화
vis = [[False for _ in range(M)] for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

# print(vis)
# print(dist)
# exit()

# 3. 시작점
x, y = 1, 2  # (열, 행)

vis[y][x] = True
dist[y][x] = 0

# 4. BFS 큐
q = deque()
q.append((y, x))


# 4방향 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

w1x,w1y = 2, 3
w2x,w2y = 2, 4
w3x, w3y = 3, 4

# 5. BFS 수행
while q:
    cy, cx = q.popleft()
    
    for d in range(4):
        ny = cy + dy[d]
        nx = cx + dx[d]
        
        if 0 <= ny < N and 0 <= nx < M and not vis[ny][nx]:
            vis[ny][nx] = True
            dist[ny][nx] = dist[cy][cx] + 1
            q.append((ny, nx))

# 6. 결과 출력
print("거리 테이블")
for row in dist:
    print(" ".join(map(str, row)))