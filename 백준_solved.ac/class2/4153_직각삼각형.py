#4153_직각삼각형
#구현, 수학
#

lst = list(map(int, input().split()))

while not (lst[0] == 0 & lst[1] == 0 & lst[2] == 0) :
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]

    if (a**2 + b ** 2 == c ** 2) :
        print("right")
    else :
        print("wrong")

    lst = list(map(int, input().split()))
