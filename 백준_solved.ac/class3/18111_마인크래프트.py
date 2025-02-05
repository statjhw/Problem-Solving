#18111_마인크래프트
#브루트포스

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

graph = []

max_h, min_h = 0, 0
for _ in range(N) :
    n = list(map(int, input().split()))
    max_v = max(n)
    min_v = min(n)
    if max_h < max_v :
        max_h = max_v
    if min_h > min_v :
        min_h = min_v
    graph.append(n)

result = []
for h in range(min_h, max_h+1) :
    time = 0
    resume = B
    for i in range(N) :
        for j in range(M) :
            diff = h - graph[i][j]
            if diff < 0 :
                resume += abs(diff)
                time += 2 * abs(diff)
            elif diff > 0 :
                resume -= diff
                time += diff
    if resume >= 0 :
        result.append([time, h, resume])

result.sort(key=lambda x : (x[0], -x[1]))
print(result[0][0], result[0][1])


#Count와 그래프 평탄화 방법 이용
# import sys
# from collections import Counter
#
# input = sys.stdin.readline
#
# N, M, B = map(int, input().split())
#
# graph = []
# max_h, min_h = 0, float('inf')
#
# for _ in range(N):
#     row = list(map(int, input().split()))
#     max_h = max(max_h, max(row))
#     min_h = min(min_h, min(row))
#     graph.extend(row)  # ✅ `sum(graph, [])` 대신 `graph`를 평탄화 (1차원 리스트)
#
# height_count = Counter(graph)  # ✅ 각 높이별 개수 저장
#
# result = []
# for h in range(min_h, max_h + 1):
#     time = 0
#     blocks = B
#
#     for height, count in height_count.items():
#         diff = height - h
#
#         if diff > 0:  # 블록 제거
#             blocks += diff * count
#             time += 2 * diff * count
#         elif diff < 0:  # 블록 추가
#             blocks -= abs(diff) * count
#             time += abs(diff) * count
#
#     if blocks >= 0:
#         result.append((time, h))
#
# result.sort(key=lambda x: (x[0], -x[1]))
# print(result[0][0], result[0][1])