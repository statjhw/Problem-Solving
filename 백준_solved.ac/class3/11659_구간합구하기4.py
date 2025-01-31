#11659_구간 합 구하기 4
#dp?

import sys

input = sys.stdin.readline

def prod_ij(lst,total, i, j) -> int :
    if j-i >= N//2 :
        result = total - sum(lst[0:i]) - sum(lst[j+1:])
    else :
        result = sum(lst[i:j+1])
    return result

lst = [0]

N, M = map(int, input().split())

lst = lst + list(map(int, input().split())) + [0]
total = sum(lst)

for _ in range(M) :
    i, j = map(int, input().split())
    print(prod_ij(lst,total, i, j))