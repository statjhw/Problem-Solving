#10250_ACM호텔.py
#수학
#O(1)
#나머지 연산에서 코너 케이스에서 문제 발생 한다. 
#해결법 : (N - 1) // H + 1로 연산하면 코너 케이스 해결 가능!
#나머지와 몫 계산 시 코너 케이스 연산 고려

test_n = int(input())

for i in range(test_n) :
    n = list(map(int, input().split()))
    floor = n[2] % n[0]
    if floor == 0 :
        floor = n[0]

    room_number = (n[2] - 1) // n[0] + 1
    print(f"{floor}{room_number:02}")

