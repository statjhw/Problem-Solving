#1654_랜선 자르기

import sys
input = sys.stdin.readline


K, N = map(int, input().split())
lst = []
for _ in range(K) :
    lst.append(int(input()))

lst.sort(reverse=True)

max_length = lst[1]
idx = 1

while 1 :
    flag = False
    total = 0
    for x in lst :
        if x >= max_length :
            total += x // max_length
            if total >= N :
                flag = True
                break
    
    if flag :
        break
    else :
        if idx <= len(lst) - 1 :
            if max_length//2 > lst[idx] :
                max_length = max_length // 2 
            else :
                max_length = lst[idx] 
                idx += 1
        else :
            max_length = max_length - 1
print(max_length)


