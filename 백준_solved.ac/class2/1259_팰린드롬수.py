#1259팰린드롬수
#구현

while (1) :
    s = input()
    if s == '0' :
        break
    par = True
    for i in range(len(s)//2) :
        if s[i] != s[len(s) - i - 1] :
            par = False;
            break
    if par : 
        print("yes")
    else :
        print("no")