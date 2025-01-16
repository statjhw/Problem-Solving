#10773_제로
#stack ->last-in-first-out

from collections import deque

K = int(input())

stack = deque()

for _ in range(K) :
    n = int(input())
    if n == 0 :
        stack.pop()
    else :
        stack.append(n)


print(sum(stack))