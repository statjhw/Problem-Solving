#1436_영화감독 숌
#브루트 포스

lst_666 = []

N = int(input())
num = 666

while len(lst_666) < N :
    if '666' in str(num) :
        lst_666.append(num)
    num += 1

print(lst_666[N-1])

            