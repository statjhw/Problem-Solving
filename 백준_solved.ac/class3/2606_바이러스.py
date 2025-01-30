#2606_바이러스
#그래프, dfs, bfs

import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(graph, node, visited) :
    visited.append(node)
    for n in graph[node] :
        if n not in visited :
            dfs(graph, n, visited)



N = int(input())
M = int(input())

graph = defaultdict(list)

#그래프 생성
for _ in range(M) :
    a, b = map(int, input().split())
    #무방향 그래프
    graph[a].append(b)
    graph[b].append(a)


visited = []

dfs(graph, 1, visited)

print(len(visited) - 1)
