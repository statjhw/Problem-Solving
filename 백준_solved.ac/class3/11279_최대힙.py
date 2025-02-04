#11279_최대 힙
#힙

import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N) :
    x = int(input())
    if x == 0 :
        if len(heap) == 0 :
            print("0")
        else :
            print(-heapq.heappop(heap))
    else :
        heapq.heappush(heap, -x)
