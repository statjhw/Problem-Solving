#11286_절댓값 힙
#힙

import sys, heapq
input = sys.stdin.readline

N = int(input())

plus_heap = []
minus_heap = []

for _ in range(N) :
    val = int(input())
    if val == 0 :
        if len(plus_heap) == 0 and len(minus_heap) == 0 :
            print("0")
        elif  len(plus_heap) == 0 and len(minus_heap) != 0 :
            print(-heapq.heappop(minus_heap))
        elif len(plus_heap) != 0 and len(minus_heap) == 0 :
            print(heapq.heappop(plus_heap))
        else :
            plus = plus_heap[0]
            minus = -minus_heap[0]
            if abs(minus) <= plus :
                print(-heapq.heappop(minus_heap))
            else :
                print(heapq.heappop(plus_heap))
    else :
        if val < 0 :
            heapq.heappush(minus_heap, -val)
        else :
            heapq.heappush(plus_heap, val)

