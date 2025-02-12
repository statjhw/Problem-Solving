#1389_케빈 베이컨의 6단계 법칙
#그래프 이론, BFS -> 최단거리 계산

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

#bfs인데 최단경로를 구해야 하는데 모든 경우에 대해서 구해야 함
#L_i의 리스트를 이용해야 함

def bfs(graph, visit, node, end) :
    path = [[node]]
    visit[node] = True
    i = 0
    while len(path[i]) != 0 :
        path.append([])
        for n in path[i] :
            for v in graph[n] :
                if not visit[v] :
                    path[i+1].append(v)
                    visit[v] = True
                    if v == end :
                        return i+1

        i = i+1
    return None


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = [-1 for _ in range(N+1)]
for i in range(1, N+1) :
    r = 0
    for j in range(1, N+1) :
        if i == j :
            continue
        else :
            visit = [False for _ in range(N + 1)]
            r += bfs(graph, visit, i, j)

    result[i] = r
