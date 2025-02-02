#17626_Four Squares
#

import sys
input = sys.stdin.readline


N = int(input())

for i in range(0, N//2, -1) :
    for j in range(0, i+1) :
        for k in range(0, j+1,) :
            for p in range(1, k+1) :
                if N == (p*p + k*k + j*j + i*i) :
                    print(p, k, j, i)