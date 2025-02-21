#6064_카잉달력
#구현

import sys
input = sys.stdin.readline

def find_kaing(M, N, x, y):
    while x <= M * N:  # M과 N의 최소공배수 이하만 확인하면 됨
        if (x - 1) % N + 1 == y:  # year % N == y 와 같은 조건
            return x
        x += M  # x를 M씩 증가시키면서 탐색
    return -1

T = int(input())
for _ in range(T) :
    M, N, x, y = map(int, input().split())
    print(find_kaing(M, N, x, y))