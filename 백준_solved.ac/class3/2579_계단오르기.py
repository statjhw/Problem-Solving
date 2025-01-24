#2579_계단 오르기
#dp

import sys
input = sys.stdin.readline

N = int(input())
score = [0]

for _ in range(N) :
    score.append(int(input()))

if N == 1 :
    print(score[1])
    sys.exit()

dp = [0] * (N + 1) #각 단계에서 최댓값!
dp[1] = score[1]
dp[2] = score[2] + dp[1]

for i in range(3, N + 1) :
    dp[i] = max(dp[i-2], dp[i-3] + score[i-1]) + score[i]

print(dp[N])