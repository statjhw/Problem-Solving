#1874_스택 수열
#스택

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sequence = [int(input()) for _ in range(N)]

arr = [i for i in range(N, 0, -1)]

stack = deque()
symbol = []

idx = 0
flag = True
while idx < N :
    if len(arr) != 0 :
        if sequence[idx] >= arr[len(arr) - 1] :
            stack.append(arr[len(arr)-1])
            symbol.append("+")
            arr.pop()

        else :
            if sequence[idx] == stack[len(stack)-1] :
                stack.pop()
                symbol.append("-")
                idx += 1
            else :
                flag = False
                break
    
    else :
        if sequence[idx] == stack[len(stack)-1] :
            stack.pop()
            symbol.append("-")
            idx += 1
        else :
            flag = False
            break
        
if flag :
    for x in symbol :
        print(x)
else :
    print("NO")