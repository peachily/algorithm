grid = []

for _ in range(9):
    line = input().split()
    numbers = list(map(int, line))
    grid.append(numbers)

answer = []

for row, list in enumerate(grid, start=1):
    for col, value in enumerate(list, start=1):
        answer.append((value, row, col))

max_value, row, col = max(answer)

print(max_value)
print(row, col)