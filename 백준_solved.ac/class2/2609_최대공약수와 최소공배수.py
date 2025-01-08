#2609_최대공약수와 최소공배수
#수학, 구현

a, b = map(int, input().split())

def GCF(a : int, b : int) -> int:
    sol = 1
    for i in range(1, min(a, b) + 1) :
        if a % i == 0 and b % i == 0 :
            sol = i
    return sol

def GDF(a : int, b : int) -> int :
    sol = max(a, b)
    while 1 :
        if sol % a == 0 and sol % b == 0 :
            break
        else :
            sol += 1
    return sol
        
print(GCF(a, b))
print(GDF(a, b))