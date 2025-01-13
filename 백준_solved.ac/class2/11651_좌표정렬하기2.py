#11651_좌표 정렬하기 2
#정렬

coordinate = []

N = int(input())

for _ in range(N) :
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x : (x[1], x[0]))

for val in coordinate :
    print(val[0], val[1])