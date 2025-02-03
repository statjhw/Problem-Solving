#2630_색종이 만들기
#분할정복, 재귀
import sys
input = sys.stdin.readline

def findn(graph, n,x, y,color, count) :
    if n == 1 :
        if graph[y][x] == color :
            return True
        else :
            return False
    else :
        a = findn(graph, n/2, x, y, color, count)
        b = findn(graph, n/2, x+int(n/2), y, color, count)
        c = findn(graph, n/2, x, int(y+n/2), color, count)
        d = findn(graph, n/2, x+int(n/2), y+int(n/2), color, count)

        if a and b and c and d :
            return True

        elif not a and not b and not c and not d :
            return False

        else :
            cnt = int(a) + int(b) + int(c) + int(d)
            count[0] += cnt
            return False


N = int(input())
graph = []
for y in range(N) :
    graph.append(list(map(int, input().split())))

count = [0]

if findn(graph, N, 0, 0, 0, count) :
    count[0] += 1
print(count[0])
count = [0]
if findn(graph, N, 0, 0, 1, count) :
    count[0] += 1
print(count[0])