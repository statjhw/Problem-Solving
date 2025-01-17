#1929_소수 구하기
#에라스토스테네스의 체
#O(nlogn) 중요

import sys
import math

input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [False for _ in range(N+1)]

def check_prime(array, x) :
    start = 2
    end = int(math.sqrt(x)) + 1
    for i in range(2, end) :
        if array[i] :   #i가 소수일 때만 체크
            if x % i == 0 :
                return
    array[x] = True
    return

for i in range(2, N+1) :
    check_prime(is_prime, i)

for i in range(M, len(is_prime)) :
    if is_prime[i] :
        print(i)
    