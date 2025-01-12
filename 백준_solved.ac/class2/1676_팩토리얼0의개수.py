#1676_팩토리얼 0개의 개수

def factorial(n) :
    sol = 1
    for i in range(1, n+1) :
        sol *= i
    return sol

n = int(input())
n = str(factorial(n))

sol = 0
for x in n[::-1] : 
    if x == '0' :
        sol += 1
    else :
        break

print(sol)