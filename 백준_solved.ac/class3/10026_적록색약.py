#10026_적록색약
#그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, visit, color=False) :
    count = 0
    for i in range(N) :
        for j in range(N) :
            if not visit[j][i] :
                    dfs_nomal(graph, visit,(i, j) , color)
                    count += 1
    return count


def dfs_nomal(graph, visit, node, color=False) :
    global dx, dy
    visit[node[1]][node[0]] = True

    for i in range(4) :
        x = node[0] + dx[i]
        y = node[1] + dy[i]

        if 0 <= x < N and 0 <= y < N :
            if not visit[y][x] :
                if not color :
                    if graph[y][x] == graph[node[1]][node[0]] :
                        dfs_nomal(graph, visit, (x, y))

                else :
                    if graph[node[1]][node[0]] == "R" or graph[node[1]][node[0]] == "G" :
                        if graph[y][x] == "R" or graph[y][x] == "G" :
                            dfs_nomal(graph, visit, (x, y), True)

                    else :
                        if graph[y][x] == graph[node[1]][node[0]] :
                            dfs_nomal(graph, visit, (x, y), True)

N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(input().strip()))

visit = [[False]*N for _ in range(N)]
nomal = dfs(graph,visit)
visit = [[False]*N for _ in range(N)]
nocolor = dfs(graph, visit, True)

print(nomal, nocolor)




