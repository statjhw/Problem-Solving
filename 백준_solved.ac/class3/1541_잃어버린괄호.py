#1541_읽어버린 괄호

import sys
import re
from collections import deque

input = sys.stdin.readline


split_chars = r"([+-])"

string = input().strip()
result = re.split(split_chars, string)

plus_count = result.count("+")


while len(result) > 1 :
    if plus_count > 0 :
        for i in range(len(result)) :
            if result[i] == "+" :
                r = int(result[i-1]) + int(result[i+1])
                result[i-1] = r
                del result[i]
                del result[i]
                break
        plus_count -= 1

    else :
        for i in range(len(result)) :
            if result[i] == "-" :
                r = int(result[i-1]) - int(result[i+1])
                result[i-1] = r
                del result[i]
                del result[i]
                break

print(result[0])