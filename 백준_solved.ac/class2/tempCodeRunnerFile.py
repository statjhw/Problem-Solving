#7568_덩치
#정렬

N = int(input())

lst = []

for i in range(N) :
    h, t = map(int, input().split())
    lst.append([h, t, i, 0])


rank = 1
same_n = 0
for i in range(N) :
    for j in range(i+1,N) :
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1] :
            lst[i], lst[j] = lst[j], lst[i]
    
    if i == 0 :
        lst[i][3] = rank
        
    else :
        if lst[i][0] < lst[i-1][0] and lst[i][1] < lst[i-1][1]:
            rank = same_n + rank + 1
            lst[i][3] = rank
            same_n = 0
            
        else :
            lst[i][3] = rank
            same_n += 1
            



lst.sort(key=lambda x : x[2])

for x in lst :
    print(x[3], end=" ")


