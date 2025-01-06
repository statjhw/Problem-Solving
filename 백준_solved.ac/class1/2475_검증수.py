#2475_검증수.py
#단순 수학
#시간복잡도 O(1)

number = list(map(int, input().split()))

sum = 0 
for i in range(len(number)) :
    sum += number[i] ** 2

r = sum % 10

print(r)