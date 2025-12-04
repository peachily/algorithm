# https://www.acmicpc.net/problem/2167

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

results = []
K = int(input())
for _ in range(K):
    I, J, X, Y = map(int, input().split())

    res = 0
    for y in range(N):
        for x in range(M):
            if I-1 <= y <= X-1 and J-1 <= x <= Y-1:
                res = res + arr[y][x]
        
    results.append(res)

print(results)
for result in results:
    print(result)
    
