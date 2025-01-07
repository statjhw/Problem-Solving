#2031_분해합
#브루트포스
#O(n)

n = int(input())
sol = 0

for i in range(1, n) :
    lst = list(str(i))
    s = i
    s += sum(map(int, lst))
    if s == n :
        sol = i
        break

print(sol)