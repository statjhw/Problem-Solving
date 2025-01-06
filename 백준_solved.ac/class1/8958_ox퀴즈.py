#8958_ox퀴즈
#구현, 문자열

test_n = int(input())

for i in range(test_n) :
    lst = list(input())
    stage_score = 1
    total_score = 0
    for i in lst :
        if i == 'O' :
            total_score += stage_score
            stage_score += 1
        else :
            stage_score = 1
    print(total_score)