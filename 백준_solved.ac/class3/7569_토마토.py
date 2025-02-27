#7569_토마토
#그래프, bfs

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

count = 0

def bfs(graph, visited, nodes) :
    global count
    """day->한번 진행 시 변경사항 적용됨
    graph -> 토마토의 상태, -1, 0, 1
    nodes -> 토마토의 상태가 1인 node의 좌표들
    """
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    for node in nodes :
        for i in range(6) :
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            z = node[2] + dz[i]

            if 0 <= x < M and 0 <= y < N and 0 <= z < H  :
                if visited[z][y][x] == False and graph[z][y][x] == -1 :
                    visited[z][y][x] == True
                    nodes.append((x,y,z))
                    count += 1
                if visited[z][y][x] == False and graph[z][y][x] == 0 :
                    visited[z][y][x] == True


graph = []
nodes = []
visited = []

for z in range(H) :
    lst = []
    visit = []
    for y in range(N) :
        l = list(map(int, input().split()))
        for x in range(len(l)) :
            if l[x] == 1 :
                nodes.append((x, y, z))
        lst.append(l)
        visit.append([False] * M)
    visited.append(visit)
    graph.append(lst)

for node in nodes :
    visited[node[2]][node[1]][node[0]] = True

count += len(nodes)
result = 0
while True :
    bfs(graph, visited, nodes)
    result += 1


