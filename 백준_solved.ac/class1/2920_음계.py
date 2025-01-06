#2920_음계
#구현
#

lst = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, len(lst)) :
    if lst[i - 1] < lst[i] :
        descending = False
    if lst[i - 1] > lst[i] :
        ascending = False

if ascending :
    print("ascending")
elif descending :
    print("descending")
else :
    print("mixed")
