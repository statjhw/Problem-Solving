#1003_피보나치 함수

import sys
input = sys.stdin.readline

def fibonacci_dp(lst, n, count) :
    if n == 0 :
        count[0] += 1
        return 0
    elif n == 1 :
        count[1] += 1
        return 1
    else :
        if lst[n][0] == -1 :
            count_new1 = [0, 0]
            count_new2 = [0, 0]
            a = fibonacci_dp(lst, n-2,count_new1) 
            b = fibonacci_dp(lst, n-1,count_new2)
            lst[n-2][0] = a 
            lst[n-1][0] = b
            lst[n-2][1], lst[n-2][2] = count_new1[0], count_new1[1]
            lst[n-1][1], lst[n-1][2] = count_new2[0], count_new2[1]
            count[0] += count_new1[0] + count_new2[0]
            count[1] += count_new1[1] + count_new2[1]
            return a + b
        else :
            count[0] += lst[n][1]
            count[1] += lst[n][2]
            return lst[n][0]

T = int(input())

for _ in range(T) :
    n = int(input())
    lst = [[-1, 0, 0] for _ in range(n+1)]
    count = [0, 0]
    fibonacci_dp(lst, n, count)
    print(count[0], count[1])