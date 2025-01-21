#11723_집합
#시간복잡도 ?

import sys
input = sys.stdin.readline

S = [False for _ in range(21)]

M = int(input())

for _ in range(M) :
    cmd = list(input().split())
    if cmd[0] == "add" :
        S[int(cmd[1])] = True

    elif cmd[0] == "remove" :
        S[int(cmd[1])] = False
    
    elif cmd[0] == "toggle" :
        if S[int(cmd[1])] == False : 
            S[int(cmd[1])] = True
        else : 
            S[int(cmd[1])] = False
    
    elif cmd[0] == "check" :
        print(int(S[int(cmd[1])]))

    elif cmd[0] == "all" :
        for i in range(len(S)) :
            S[i] = True
    
    elif cmd[0] == "empty" :
        for i in range(1,len(S)) :
            S[i] = False

    else :
        pass