#30802_웰컴키트
#구현, 수학

n = int(input())
lst = list(map(int, input().split()))
T_P = list(map(int, input().split()))
T = T_P[0]
P = T_P[1]


tshirt = 0
pen = 0
r = 0

for i in lst :
    if i == 0 :
        continue
    tshirt += ( (i-1) // T + 1)   #T의 배수 일 때 + 1되기 때문에 i - 1을 나누어야 함함

pen = ( n // P)
r = (n % P)

print(tshirt)
print(pen, r)