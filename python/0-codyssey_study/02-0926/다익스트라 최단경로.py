# 백준 1753 최단거리
# https://www.acmicpc.net/problem/1753

# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
# u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.



import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  # 무한대 값 (도달 불가를 표시)

# 입력
V, E = map(int, input().split())   # V: 정점 개수, E: 간선 개수
K = int(input())   # 시작 정점 번호
graph = [[] for _ in range(V + 1)]   # 인접 리스트 (1번부터 V번까지 사용)
distance = [INF] * (V + 1)           # 최단 거리 테이블

# 간선 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # (도착 노드, 가중치)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        # 인접 노드 확인
        for next_node, w in graph[now]:
            cost = dist + w
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

# 실행
dijkstra(K)

# 출력
for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else "INF")