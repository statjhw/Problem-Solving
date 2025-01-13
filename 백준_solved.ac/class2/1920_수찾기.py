#1920_수 찾기
#서치
#시간 복잡도 계산 필요 -> O(n^2)은 시간 초과

import sys
import math
N = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().split()))

A.sort()

def binary_sreach(arr, target) :
    low = 0
    high = len(arr) - 1 

    while (low <= high) :
        mid = math.floor((low + high) / 2)
        if arr[mid] == target :
            return True
        elif arr[mid] < target :
            low = mid + 1
        else : 
            high = mid - 1
     
    return False

for x in lst :
    if binary_sreach(A, x) :
        print("1")
    else :
        print("0")
            