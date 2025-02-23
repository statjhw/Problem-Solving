#11403_경로 찾기
#그래프

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

incident_matrix = []

for _ in range(N) :
    incident_matrix.append(list(map(int, input().split())))

def search_i(matrix, i) :
    queue = deque([i])
    visit = [0 for _ in range(N)]

    while queue :
        node = queue.popleft()
        for n in range(N) :
            if matrix[node][n] == 1 and visit[n] == 0 :
                queue.append(n)
                visit[n] = 1

    return visit


result = []
for i in range(N) :
    result.append(search_i(incident_matrix, i))

for i in range(N) :
    for j in range(N) :
        print(result[i][j], end=" ")
    print()