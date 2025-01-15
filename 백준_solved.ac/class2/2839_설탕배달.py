#2839_설탕 배달
#브루트 포스 알고리즘?
import math

N = int(input())

max_5 = N // 5 
max_3 = N // 3

lst = []

for i in range(max_5+1) :
    for j in range(max_3+1) :
        total = i * 5 + j * 3
        if total == N :
            lst.append([i, j, i+j])


lst.sort(key=lambda x : x[2])

if len(lst) == 0 :
    print(-1)
else :
    print(lst[0][2])
