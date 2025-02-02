#1012_유기농배추
#그래프, dfs(깊이 우선 탐색)이용

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가
input = sys.stdin.readline

def dfs(graph, visit) -> int :
    count = 0
    for node in graph :
        if node in visit :
            continue
        else :
            dfs_node(graph, visit, node)
            count += 1
    return count

def dfs_node(graph, visit, node) :
    visit.append(node)
    incident = [[node[0]-1, node[1]], [node[0]+1, node[1]], \
                [node[0], node[1]-1],[node[0], node[1]+1]]

    for incident_node in incident :
        if incident_node in graph :
            if incident_node not in visit :
                dfs_node(graph, visit, incident_node)


T = int(input())

for _ in range(T) :
    M, N, K = map(int, input().split())
    graph = []
    for _ in range(K) :
        graph.append(list(map(int, input().split())))
    visit = []
    print(dfs(graph, visit))
