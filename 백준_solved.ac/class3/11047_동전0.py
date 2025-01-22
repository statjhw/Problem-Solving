#11047_동전 0 
#그리디

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

A = []

for _ in range(N) :
    A.append(int(input()))

total = 0

while K > 0 :
    coin = A.pop()
    if K >= coin :
        total += K // coin
        K = K % coin

print(total)