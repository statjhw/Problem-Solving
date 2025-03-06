#7576_토마토
#그래프, 너비우선탐색

from collections import deque
import sys

input = sys.stdin.readline


M, N = map(int, input().split())
count = 0

def bfs(graph, nodes) :
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    days = {}
    for node in nodes :
        days[node] = 0
    queue = deque(nodes)

    while queue :
        node = queue.popleft()
        for i in range(4) :
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            if 0 <= x < M and 0 <= y < N :
                if graph[y][x] == 0 :
                    days[(x, y)] = days[node] + 1
                    graph[y][x] = 1
                    queue.append((x, y))
                    count += 1
    return max(days.values())


graph = []
nodes = []
total = 0
for y in range(N) :
    lst = list(map(int, input().split()))
    for x in range(len(lst)) :
        if lst[x] == 0 or lst[x] == 1 :
            total += 1
        if lst[x] == 1 :
          nodes.append((x, y))
    graph.append(lst)

count += len(nodes)

if count == total :
    print("0")
    sys.exit()

if len(nodes) == 0 :
    print("-1")
    sys.exit()

max_value = bfs(graph, nodes)

if count == total :
    print(max_value)
else :
    print("-1")


