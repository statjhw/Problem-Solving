#18110_solved.ac
#

import sys

def half_up(val) :
    if val - int(val) >= 0.5 :
        val = int(val) + 1
    else :
        val = int(val)
    return val



input = sys.stdin.readline

N = int(input())

score = []

for _ in range(N) :
    score.append(int(input()))


mean = 0

if N == 0 :
    pass
elif N == 1 or N == 2 or N == 3 :
    mean = sum(score) / len(score)
    mean = half_up(mean)
else :
    pivot = 0.15 * N
    pivot = half_up(pivot)
    score.sort()
    score = score[pivot:N-pivot]
    mean = sum(score) / len(score)
    mean = half_up(mean)

print(mean)