n = int(input())
target = int(input())

board = [[0] * n for _ in range(n)]

x = y = n // 2
board[x][y] = 1

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 2
step = 1
direction = 0

while num <= n * n:
    for _ in range(2):
        dx, dy = dirs[direction % 4]
        for _ in range(step):
            if num > n * n:
                break
            x += dx
            y += dy
            board[x][y] = num
            num += 1
        direction += 1
    step += 1

tx = ty = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == target:
            tx = i + 1
            ty = j + 1

for row in board:
    print(*row)
print(tx, ty)
