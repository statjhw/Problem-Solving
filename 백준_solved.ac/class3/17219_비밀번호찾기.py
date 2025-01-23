#17219_비밀번호 찾기 
# 해쉬테이블
import sys 
from collections import defaultdict 

input = sys.stdin.readline  

N, M = map(int, input().strip().split()) 
search_pw = defaultdict(str)  

for _ in range(N) :     
    key, value = input().strip().split()     
    search_pw[key] = value  

for _ in range(M) :     
    key = input().strip()     
    print(search_pw[key]) 