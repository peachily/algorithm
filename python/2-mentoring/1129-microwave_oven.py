# https://www.acmicpc.net/problem/14470

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0

if A < 0:
    time = ((0-A) * C) + D + (B * E)

else:
    time = (B-A) * E

print(time)