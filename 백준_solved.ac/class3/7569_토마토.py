#7569_토마토
#그래프, bfs

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

count = 0

def bfs(graph, nodes) :
    global count
    """day->한번 진행 시 변경사항 적용됨
    graph -> 토마토의 상태, -1, 0, 1
    nodes -> 토마토의 상태가 1인 node의 좌표들
    """
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    count = len(nodes)
    queue = deque(nodes)
    days = {}
    for node in nodes :
        days[node] = 0
    max = 0

    while queue :
        node = queue.popleft()
        for i in range(6) :
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            z = node[2] + dz[i]
            if 0 <= x < M and 0 <= y < N and 0 <= z < H :
                if graph[z][y][x] == 0 :
                    graph[z][y][x] = 1
                    queue.append((x, y, z))
                    days[(x, y, z)] = days[node] + 1
                    if max < days[(x, y, z)] :
                        max = days[(x, y, z)]
                    count += 1

    return max

graph = []
nodes = []
total = 0
for z in range(H) :
    lst = []
    for y in range(N) :
        l = list(map(int, input().split()))
        for x in range(len(l)) :
            if l[x] == 1 :
                nodes.append((x, y, z))
            if l[x] == 1 or l[x] == 0 :
                total += 1
        lst.append(l)
    graph.append(lst)

if total == len(nodes) :
    print("0")
    sys.exit()


max = bfs(graph, nodes)

if total == count :
    print(max)
else :
    print("-1")



