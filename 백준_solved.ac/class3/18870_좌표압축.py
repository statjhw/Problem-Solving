#18870_좌표압축
#정렬

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
dic = Counter(lst)

sorted_dic = dict(sorted(dic.items()))

for i, k in enumerate(sorted_dic.keys()) :
    sorted_dic[k] = i

for x in lst :
    print(sorted_dic[x], end=" ")