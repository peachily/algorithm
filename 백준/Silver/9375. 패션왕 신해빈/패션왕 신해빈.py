T = int(input())

for _ in range(T):
    n = int(input())
    clothes = {}
    type = set()

    for _ in range(n):
        name, kind = input().split()
        type.add(kind)
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    
    answer = 1
    for kind in type:
        answer = (clothes[kind] + 1) * answer
    
    print(answer -1)
