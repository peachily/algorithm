n = int(input())

staying = set()

for _ in range(n):
    employee, status = input().split()

    if status == "enter":
        staying.add(employee)
    elif status == "leave":
        staying.discard(employee)

answer = sorted(staying, reverse=True)

for names in answer:
    print(names)