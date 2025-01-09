#11050_이항 계수 1

import sys

n, k = map(int, sys.stdin.readline().split())

sol = 1
loop = n

for i in range(k) :
    sol *= loop
    loop -= 1

b = 1
for i in range(1, k+1) :
    b *= i

sol = sol / b
print(int(sol))