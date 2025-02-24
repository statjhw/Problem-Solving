#14940_쉬운 최단거리
#그래프, 너비우선탐색 -> 최단경로

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(n) :
    lst = list(map(int, input().split()))
    graph.append(lst)
    if 2 in lst :
        for j in range(len(lst)) :
            if lst[j] == 2 :
                start = (i, j)
                break

def bfs_distance(graph, start) :
    global dx, dy
    distances = [[-1]*m for _ in range(n)]
    start_x, start_y = start
    distances[start_x][start_y] = 0
    queue = deque([(start)])

    while queue :
        node = queue.popleft()
        x, y = node

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < m :
                if  distances[nx][ny] == -1 and graph[nx][ny] == 1 :
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))

    return distances

result = bfs_distance(graph, start)
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            result[i][j] = 0

for i in range(n) :
    for j in range(m) :
        print(result[i][j], end=" ")
    print()
