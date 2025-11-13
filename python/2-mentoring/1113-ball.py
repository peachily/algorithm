# https://www.acmicpc.net/problem/1547

number = int(input())

ball = 1

for n in range(number):
    x, y = map(int, input().split())
    if ball == x:
        ball = y
    elif ball == y:
        ball = x

print(ball)