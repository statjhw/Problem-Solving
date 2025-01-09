#28702_FizzBuzz
#구현

first = input()
second = input()
third = input()

output = ""
if first == "Fizz" :
    if second == "Buzz" :
        output = "Fizz"
    else :
        if (int(second) + 2) % 5 == 0 :
            output = "FizzBuzz"
        else :
            output = "Fizz"
elif first == "FizzBuzz" :
    output = "Fizz"
elif first == "Buzz" :
    if second == "Fizz" :
        output = int(third) + 1
    else :
        if third == "Fizz" :
            output = int(second) + 2
        else :
            output = "Fizz"
else :
    if second == "Fizz" :
        if third == "Buzz" :
            output = int(first) + 3
        else :
            if (int(third) + 1) % 5 == 0 :
                output = 'Buzz'
            else :
                output = int(third) + 1
    elif second == "FizzBuzz" :
            output = int(third) + 1
    elif second == "Buzz" :
        if third == "Fizz" :
            output = int(first) + 3
        else :
            output = "Fizz"
    else :
        if third == "FizzBuzz" :
            output = int(second) + 2
        else : 
            if (int(second) + 2) % 5 == 0 :
                output = "Buzz"
            else :
                output = int(second) + 2

print(output)
