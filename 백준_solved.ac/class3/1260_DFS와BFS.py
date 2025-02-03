#1260_DFS와 BFS
#그래프, dfs, bfs

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(graph, visit, node) :
    visit[node] = True
    print(node, end=" ")
    for n in graph[node] :
        if not visit[n] :
            dfs(graph, visit, n)

def bfs(graph, visit, node) :
    queue = deque([node])
    visit[node] = True

    while queue :
        v = queue.popleft()
        print(v, end= " ")
        for i in graph[v] :
            if not visit[i] :
                queue.append(i)
                visit[i] = True

N, M, V = map(int, input().split())

graph = defaultdict(list)
visit = [False for _ in range(N+1)]

for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1) :
    graph[i].sort()

dfs(graph, visit, V)
print()
visit = [False for _ in range(N+1)]
bfs(graph, visit, V)
