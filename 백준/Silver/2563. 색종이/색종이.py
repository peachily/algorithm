def solve():
    blank = [[0] * 100 for _ in range(100)]

    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())

        top = 99 - y - 9
        bottom = 99 - y
        left = x
        right = x + 9

        for row in range(top, bottom+1):
            for col in range(left, right+1):
                blank[row][col] = 1

    answer = sum(sum(row) for row in blank)

    return answer

print(solve())
