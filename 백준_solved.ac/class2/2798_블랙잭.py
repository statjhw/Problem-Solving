#2798_블랙잭
#브루트포스

n, m = map(int, input().split())
lst = list(map(int, input().split()))

sol = 0
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum = lst[i] + lst[j] + lst[k]
            if sum > m :
                pass
            else :
                if sum > sol :
                    sol = sum

print(sol)
