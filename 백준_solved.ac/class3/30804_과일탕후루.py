#30804_과일탕후루
#브루트포스, 슬라이딩 윈도우
#O(nlogn)

import sys
from collections import Counter, deque
from itertools import islice
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

left = 0
max_length = 0
counter = Counter()

for right in range(N) :
    counter[lst[right]] += 1

    while len(counter) > 2 :
        counter[lst[left]] -= 1
        if counter[lst[left]] == 0 :
            del counter[lst[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)