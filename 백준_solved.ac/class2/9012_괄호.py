#9012_괄호
#스택
from collections import deque

N = int(input())

for _ in range(N) :
    vps = input()
    check_stack = deque()
    
    flag = True
    for x in vps :
        if x == "(" :
            check_stack.append(x)
        elif x == ")" :
            if len(check_stack) == 0 :
                flag = False
                break
            else :
                if check_stack.pop() != "(" :
                    flag = False
                    break
    
    if flag and len(check_stack) == 0 :
        print("YES")
    else :
        print("NO")