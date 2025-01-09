#2869_달팽이는 올라가고 싶다.
#
#O(1) or O(log n)

A, B, V = map(int, input().split())

day = (V - A) / (A - B) 

if day - int(day) != 0 :
    day = int(day) + 1
day = day + 1

print(int(day))