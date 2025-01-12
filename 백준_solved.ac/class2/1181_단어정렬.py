#1181_단어 정렬
#정렬
#O(n**2)

def sort_rule(str1) :
    return (len(str1), str1)

n = int(input())
lst = []

for _ in range(n) :
    str = input()
    if lst.count(str) == 0 : #or set함수 이용
        lst.append(str)

lst.sort(key=sort_rule)

for i in lst :
    print(i)

    

