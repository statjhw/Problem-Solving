#7662_이중 우선순위 큐
#우선순위 큐
#O(logn) -> 최댓값 삭제 시 O(n) 허용하지 않음

#삭제 연산 시 최댓값 또는 최솟값은 O(1)으로 처리할 수 있지만 
#나머지는 탐색해야 함 -> 시간 초과 발생


import heapq
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T) :
    K = int(input())
    for _ in range(K) :
        cmd, val = map(int, input().split())
        val = int(val)
    
    max_heap = []   #-1를 붙여서 연산
    min_heap = []

    if cmd == "I" :
        heapq.heappush(max_heap, -val)
        heapq.heappush(min_heap, val)

    else :
        if max_heap and min_heap :    
            if val == "1" :     #최댓값을 제거
                remove_val = -heapq.heappop(max_heap)
                
            else :      #최솟값을 제거
                pass

        else :  #heap이 비어있는 경우
            continue
            



