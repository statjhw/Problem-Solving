#1074_Z
#분할정복


import sys
input = sys.stdin.readline

N, row, col = map(int, input().split())

count = 0  # 방문한 칸의 개수

def solution(n, r, c):
    global count

    if n == 0:  # 크기가 1x1이면 종료
        return

    size = 2 ** (n - 1)  # 현재 Z 배열의 한 변의 절반 크기
    if row < r + size and col < c + size:  # 1사분면 (좌상)
        solution(n - 1, r, c)
    elif row < r + size and col >= c + size:  # 2사분면 (우상)
        count += size * size  # 1사분면을 건너뜀
        solution(n - 1, r, c + size)
    elif row >= r + size and col < c + size:  # 3사분면 (좌하)
        count += 2 * size * size  # 1, 2사분면을 건너뜀
        solution(n - 1, r + size, c)
    else:  # 4사분면 (우하)
        count += 3 * size * size  # 1, 2, 3사분면을 건너뜀
        solution(n - 1, r + size, c + size)

solution(N, 0, 0)
print(count)