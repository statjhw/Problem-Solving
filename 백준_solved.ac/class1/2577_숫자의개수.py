#2577_숫자의 개수
#수학 구현
#O(logN)

A = int(input())
B = int(input())
C = int(input())

r = A * B * C

dict = {i : 0 for i in range(10)}

while (1) :
    if r == 0 :
        break;

    d = r % 10
    r = r // 10

    dict[d] += 1

for i in dict.values() :
    print(i)