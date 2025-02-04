#11724_연결 요소의 개수
#그래프

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_n(edges, visited, node) :
    visited[node] = True
    for n in edges[node] :
        if visited[n] == False :
            dfs_n(edges, visited, n)

def dfs(edges, visited) :
    count = 0
    for i in range(1, N+1) :
        if visited[i] == False :
            dfs_n(edges, visited, i)
            count += 1
    return count

N, M = map(int, input().split())

edges = defaultdict(list)

for _ in range(M) :
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

visited = [False for i in range(N+1)]

print(dfs(edges, visited))
