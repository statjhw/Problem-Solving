#2869_달팽이는 올라가고 싶다.
#
#O(1) or O(log n)

A, B, V = map(int, input().split())

day = (V - A) // (A - B) + 1

if (V - A) < (A - B) :
    day = 2

print(day)