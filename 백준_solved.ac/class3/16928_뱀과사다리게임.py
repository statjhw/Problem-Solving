#16928_뱀과사다리게임
#그래프, bfs

from collections import deque
import sys


def bfs(game) :
    dice = [1, 2, 3, 4, 5, 6]
    queue = deque([1])
    distances = {1 : 0}

    while queue :
        node = queue.popleft()
        for i in dice :
            next_node = node + i
            if next_node in game :      #사다리나 뱀이 존재하는 경우
                next_node = game[next_node][1]
            if next_node <= 100 and next_node not in distances :
                distances[next_node] = distances[node] + 1
                queue.append(next_node)

    return distances[100]

N, M = map(int, input().split())

game = dict()
for _ in range(N) :
    start, end = map(int, input().split())
    game[start] = (True, end)
for _ in range(M) :
    start, end = map(int, input().split())
    game[start] = [False, end]

result = bfs(game)
print(result)