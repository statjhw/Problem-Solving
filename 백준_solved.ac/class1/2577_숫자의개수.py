#2577_숫자의 개수
#수학 구현
#O(logN)

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C)) #문자열을 리스트로 변환 시에는 각 요소가 분리된다.

for i in range(10) :
    print(result.count(str(i)))
