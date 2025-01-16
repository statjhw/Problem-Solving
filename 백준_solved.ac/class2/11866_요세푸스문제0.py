#11866_요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

iteration = K - 1
sol = list()

while 1 :
    sol.append(lst[iteration])
    del lst[iteration]
    if len(lst) == 0 : 
        break
    iteration = (iteration + (K - 1)) % len(lst)

print("<", end="")
for i in range(len(sol)) :
    if i == len(sol)-1 :
        print(f"{sol[i]}>")
    else :
        print(f"{sol[i]}, ", end="")