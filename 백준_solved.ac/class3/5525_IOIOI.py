#5525_IOIOI
#시간복잡도: O(nlogn)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
# 1. I인 것을 찾기
# 2. I인 것을 찾으면 Pn인지 확인
# 3. 맞다면 -> 다음 2개의 OI인지 확인
#   -> OI가 맞으면 +1 하고 또 3반복
#   -> OI이 아니라면 idx를 다시 I부터 시작

def is_pn(S, n) :
    length = 2*n+1
    result = True
    for i in range(length) :
        if i % 2== 0 :
            if S[i] == "O" :
                result = False
                break
        else :
            if S[i] == "I" :
                result = False
                break
    return result

idx = 0
cnt = 0
while idx <= M - (2*N+1) :
    if S[idx] == "O" :
        idx += 1
        continue
    else :
        substr = S[idx:idx+(2*N+1)]
        if is_pn(substr, N) :
            idx += 2
            cnt += 1
        else :
            idx += 1
            continue

print(cnt)