#1389_케빈 베이컨의 6단계 법칙
#그래프 이론, BFS -> 최단거리 계산

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs_min_path(graph, start, end) -> int :
    """return : start와 end가 거쳐야하는 길의 크기의 최솟값"""
    queue = deque([start])
    distance = {start: 0}

    while queue :
        node = queue.popleft()
        for neighbor in graph[node] :
            if neighbor not in distance :
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance.get(end, -1)



N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0 for _ in range(N+1)]
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if i == j :
            continue
        else :
            value = bfs_min_path(graph, i, j)
            result[i] += value


min_idx = 1
min_value = result[1]

for i in range(2, N+1) :
    if min_value > result[i] :
        min_idx = i
        min_value = result[i]

print(min_idx)