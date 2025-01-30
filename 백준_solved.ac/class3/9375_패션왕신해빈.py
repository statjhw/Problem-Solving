#9375_패션왕 신해빈

import sys
from itertools import combinations
from collections import defaultdict
from math import prod
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    dic = defaultdict(int)
    n = int(input())

    for _ in range(n) :
        value, key = input().strip().split()
        dic[key] += 1

    values = dic.values()

    total = 1

    total = prod([value+1 for value in values]) - 1

    print(total)