#1931_회의실 배정
#그리디 알고리즘 -> O(n)이고 순서대로 담을 수 있는 데이터 형태로 변환해야 한다.

import sys
input = sys.stdin.readline

times = []
N = int(input())

for _ in range(N) :
    times.append(tuple(map(int,input().split())))

times.sort(key = lambda x : (x[1], x[0]))


start, end = times[0]
max = 1
for i in range(1, N) :
    s, e = times[i]
    if end <= s :
        start, end = s, e
        max += 1

print(max)