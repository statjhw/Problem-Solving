#1654_랜선 자르기
#시간복잡도 O(nlogn)
import sys
import math
input = sys.stdin.readline


K, N = map(int, input().split())
lst = []
for _ in range(K) :
    lst.append(int(input()))

lst.sort()

start, end = 1, max(lst)
result = 0

while start <= end :
    value = 0
    mid = (start + end) // 2
    
    for x in lst :
        value += x // mid
    if value < N :
        end = mid - 1 
    else :
        result = mid 
        start = mid + 1

print(result)