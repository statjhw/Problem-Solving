#1620_나는야 포켓몬 마스터 이다솜
#hash-table

import sys 
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_list_str = defaultdict(str)
pokemon_list_int = defaultdict(int)

for i in range(1, N+1) :
    x = input().strip()
    pokemon_list_str[i] = x
    pokemon_list_int[x] = i

for _ in range(M) :
    cmd = input().strip()
    if cmd.strip().isdigit() :
        print(pokemon_list_str[int(cmd)])
    else :
        print(pokemon_list_int[cmd])
