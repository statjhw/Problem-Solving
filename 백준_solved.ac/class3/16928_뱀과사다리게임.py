#16928_뱀과사다리게임
#그래프, bfs

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
game = dict()

for _ in range(N) :
    start, end = map(int, input().split())
    game[start] = [True, end]

for _ in range(M) :
    start, end = map(int, input().split())
    game[start] = [False, end]

def bfs(game) :
    dice = [1, 2, 3, 4, 5, 6]
    queue = deque([1])
    distances = {1 : 0}

    while queue :
        node = queue.popleft()
        for x in dice :
            next_node = node + x
            if next_node <= 100 :
                if next_node not in distances :
                    if next_node in game :
                        if game[next_node][0] :
                            next_next_node = game[next_node][1]
                            distances[next_node] = 1 + distances[node]
                            distances[next_next_node] = 1 + distances[node]
                            queue.append(next_next_node)
                        else :
                            next_next_node = game[next_node][1]
                            if next_next_node not in distances :
                                distances[next_node] = 1 + distances[node]
                                distances[next_next_node] = 1 + distances[node]
                                queue.append(next_next_node)
                    else :
                        distances[next_node] = 1 + distances[node]
                        queue.append(next_node)

    return distances[100]

result = bfs(game)
print(result)


