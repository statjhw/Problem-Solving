#2751_수 정렬하기 2
#heap 정렬
#O(nlogn)

import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = []

for _ in range(N) :
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

for _ in range(N) :
    print(heapq.heappop(heap))