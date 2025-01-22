#11399_ATM
#브루트포스

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))

lst.sort()

cumulative = 0
total = 0

for x in lst :
    total += cumulative + x 
    cumulative += x

print(total)