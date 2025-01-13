#7568_덩치
#정렬
#직접 정렬을 구현 -> 자신보다 큰 경우가 있으면 rank를 늘리기
N = int(input())

lst = []

for i in range(N) :
    h, t = map(int, input().split())
    lst.append([h, t, 1])


for  i in range(N) :
    for j in range(N) :
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1] :
            lst[i][2] += 1

for x in lst :
    print(x[2], end=" ")
