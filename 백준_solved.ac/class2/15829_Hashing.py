#15829_Hashing
#해쉬
#알파벳의 숫자 변환 -> ord함수이용 'a' -> 97, 'z' -> 122

r = 31
M = 1234567891

n = int(input())
lst = list(input())

H = 0
for i in range(len(lst)) :
    H += (ord(lst[i]) - 96) * (r ** i)

H = H % M
print(H)