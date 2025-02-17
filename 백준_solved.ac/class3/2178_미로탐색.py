#2178_미로탐색
#그래프, bfs

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def bfs(graph) :
    queue = deque([(1, 1)])
    distances = {(1, 1) : 0}

    while queue :
        node = queue.popleft()
        x, y = node
        x -= 1
        y -= 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for  i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == "1" and (nx+1, ny+1) not in distances:
                distances[(nx+1, ny+1)] = distances[(x+1, y+1)] + 1
                queue.append(((nx+1, ny+1)))
    return distances.get((N, M), -1)


graph = []
for _ in range(N) :
    graph.append(list(input().strip()))

print(bfs(graph) + 1)