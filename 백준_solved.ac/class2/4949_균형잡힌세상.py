#4949_균형잡힌 세상
#스택
from collections import deque

string = input()

while string != "." :
    check_stack = deque()
    flag = True
    for x in string :
        if x == "(" or x == "[" :
            check_stack.append(x)
        elif x == ")" :
            if len(check_stack) == 0 :
                flag = False
                break
            val = check_stack.pop()
            if  val == "(" :
                pass
            else :
                flag = False
                break
        elif x == "]" :
            if len(check_stack) == 0 :
                flag = False 
                break
            val = check_stack.pop()
            if  val == "[" :
                pass
            else :
                flag = False
                break
    
    if len(check_stack) == 0 and flag:
        print("yes")
    else :
        print("no")

    string = input()
                
