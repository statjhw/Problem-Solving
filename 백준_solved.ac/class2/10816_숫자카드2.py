#10816_숫자 카드 2
#
from collections import defaultdict

lst = defaultdict(int)

N = int(input())

n_lst = list(map(int, input().split()))

for x in n_lst :
    lst[x] += 1

M = int(input())
m_lst = n_lst = list(map(int, input().split()))

for x in m_lst :
    print(lst[x], end=" ")
    
