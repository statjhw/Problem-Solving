#1463_1로 만들기
#그리디?

import sys
from collections import defaultdict
input = sys.stdin.readline 

x = int(input())
cnt = 0 

dp = defaultdict(int)
dp[2] = 1
dp[3] = 1

for i in range(3, x) :
    if dp[i] != 0 :
        if dp[i+1] == 0 :
            dp[i+1] = dp[i] + 1
        else :
            if dp[i+1] > dp[i]+1 :
                dp[i+1] = dp[i] + 1
        if dp[2*i] == 0 :
            dp[2*i] = dp[i] + 1
        else :
            if dp[2*i] > dp[i]+1 :
                dp[2*i] = dp[i] + 1
        if dp[3*i] == 0 :
            dp[3*i] = dp[i] + 1
        else :
            if dp[3*i] > dp[i]+1 :
                dp[3*i] = dp[i] + 1

print(dp[x])

