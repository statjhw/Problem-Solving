#10989_수 정렬하기 3
#계수정렬, 메모리, 시간모두 초과될 수 있음
#O(nlogn)

import sys
def input() :
    return sys.stdin.readline()

n = int(input())

lst = [0] * 100001

for _ in range(n) :
    lst[int(input())] += 1

for i in range(n) :
    if lst[i] != 0 :
        for _ in range(lst[i]) :
            print(i)
