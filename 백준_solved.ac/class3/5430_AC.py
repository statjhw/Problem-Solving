#5430_AC
#문자열, deque

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    string = list(input().strip())
    N = int(input())
    arr = input().strip()
    if N == 0 :
        if "D" in string :
            print("error")
        else :
            print("[]")
        continue

    arr = arr[1:-1]
    arr = list(map(int, arr.split(',')))
    arr = deque(arr)
    front = True
    error = False
    for s in string :
        if s == "R" :
            if front :
                front = False
            else :
                front = True
        else : #s=="D"
            if len(arr) == 0 :
                error = True
                break
            else :
                if front :
                    arr.popleft()
                else :
                    arr.pop()

    if error :
        print("error")
    else :
        if len(arr) == 0 :
            print("[]")
        else :
            if front :
                print("[", end="")
                for i in range(len(arr) - 1) :
                    print(arr[i], end=",")
                print(f"{arr[len(arr)-1]}]")

            else :
                print("[",end="")
                for i in range(len(arr) - 1):
                    print(arr[len(arr)-1-i], end=",")
                print(f"{arr[0]}]")
