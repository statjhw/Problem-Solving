#2667_단지번호붙이기
#그래프 이론, dfs

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def dfs(graph) :
    global count
    lst = []
    cnt = 0
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] == "1":
                lst.append(dfs_node(graph, (i, j)))
                cnt += 1
    return (lst, cnt)

def dfs_node(graph, node) :
    count = 1
    x, y = node
    graph[x][y] = "0"
    stack = deque([(x, y)])

    while stack :
        x, y = stack.pop()
        for i in range(4) :
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == "1" :
                graph[nx][ny] = "0"
                stack.append((nx, ny))
                count += 1

    return count




N = int(input())
graph = []

for _ in range(N) :
    graph.append(list(input()))


lst, cnt = dfs(graph)

lst.sort()
print(cnt)

for l in lst :
    print(l)