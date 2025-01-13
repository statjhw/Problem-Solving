#10814_나이순 정렬
#정렬 -> 파이썬 sort는 stable sort

N = int(input())

lst = []

for _ in range(N) :
    age, name = tuple(input().split())
    lst.append([int(age), name])

lst.sort(key=lambda x : x[0])

for x in lst :
    print(x[0], x[1])

