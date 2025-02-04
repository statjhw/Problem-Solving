#2805_나무 자르기
#이분탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

low = 0
high = max(lst)

while low < high :
    mid = (low + high + 1) // 2
    total = 0
    for x in lst :
        length = x - mid
        if length > 0 :
            total += length
        if total > M :
            break
    if total < M :
        high = mid - 1
    else :
        low = mid


print(low)