#21736_헌내기는 친구가 필요해
#그래프, dfs

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited) :
    count = [0]
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == "I" :
                start = (i, j)

    dfs_n(graph, visited, start, count)
    return count[0]
def dfs_n(graph, visited, node, count) :
    visited.add(node)
    if graph[node[0]][node[1]] == "P" :
        count[0] += 1

    nodes = [(node[0]+1, node[1]), (node[0], node[1]+1),
             (node[0]-1, node[1]), (node[0], node[1]-1)]

    for n in nodes :
        if not (n[0] < 0 or n[1] < 0 or n[0] >= N or n[1] >= M) :
            if graph[n[0]][n[1]] == "X" :
                pass
            else :
                if n not in visited :
                    dfs_n(graph, visited, n, count)

N, M = map(int, input().split())

graph = []
for _ in range(N) :
    graph.append(list(input()))

visited = set()

c = dfs(graph, visited)
if c==0 :
    print("TT")
else :
    print(c)



