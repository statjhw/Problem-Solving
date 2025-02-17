#1697_숨바꼭질
#그래프, 너비우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end) :
    if start == end :
        return 0
    queue = deque([start])
    distances = [-1] * 100_001
    distances[start] = 0
    while queue :
        node = queue.popleft()
        for neighbor in (node-1, node+1, node*2) :
            if 0 <= neighbor <= 100_000 and distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
                if neighbor == end :
                    return distances[end]


start, end = map(int, input().split())

print(bfs(start, end))