from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            answer += 1

            q = deque()
            q.append(i)
            visited[i] = True

            while q:
                cur = q.popleft()

                for next in range(n):
                    if computers[cur][next] == 1 and not visited[next]:
                        visited[next] = True
                        q.append(next)

    return answer
