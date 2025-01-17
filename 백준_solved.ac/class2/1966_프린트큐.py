#1966_프린터 큐
#큐

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    printer = deque()
    for i in range(len(lst)) :
        if i == M :
            printer.append([lst[i], 1])
        else :
            printer.append([lst[i], 0])
    
    cnt = 0
    while len(printer) > 0 :  
        flag = True
        for i in range(1, len(printer)) :
            if printer[0][0] < printer[i][0] :
                flag = False 
                printer.rotate(-1)
                break
        
        if flag :
            cnt += 1
            if printer[0][1] == 1 :
                print(cnt)
                printer.popleft()
                break
            else :
                printer.popleft()
            
        



