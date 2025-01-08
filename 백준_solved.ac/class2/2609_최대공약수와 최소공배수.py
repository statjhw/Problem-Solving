#2609_최대공약수와 최소공배수
#수학, 구현

a, b = map(int, input().split())

def gcd(a : int, b : int) -> int :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))