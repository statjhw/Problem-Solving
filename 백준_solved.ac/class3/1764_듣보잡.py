#1764_듣보잡
#해쉬를 이용
#시간 복잡도

import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().strip().split())

lst = defaultdict(int)

for _ in range(N) :
    key = input().strip()
    lst[key] += 1

for _ in range(M) :
    key = input().strip()
    lst[key] += 1

sol = []
for x in lst.items() :
    key, value = x
    if value == 2 :
        sol.append(key)

sol.sort()
print(len(sol))
for x in sol :
    print(x)
