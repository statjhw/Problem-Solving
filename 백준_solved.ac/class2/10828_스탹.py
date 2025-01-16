#10828_스택
#스택
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N) :
    cmd = list(input().split())
    
    if cmd[0] == "push" :
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            x = stack.pop()
            print(x)
    elif cmd[0] == "size" :
        print(len(stack))
    elif cmd[0] == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif cmd[0] == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            idx = len(stack) - 1
            print(stack[idx])

        