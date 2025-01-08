#2775_부녀회장이 될테야
#재귀 함수 이용

# try 1 : 시간 초과 -> 재귀함수이용해서?
# def sum_apt(k : int, n : int) -> int : 
#     if k == 0 :
#         return n
#     else :
#         sol = 0
#         for i in range(1, n+1) :
#             sol += sum_apt(k-1, i)  
#         return sol

# try 2 : dp 이용 -> 시간초과
# def sum_apt(lst, k : int, n : int) -> int : 
#     if k == 0 :
#         return n
#     if lst[k][n] != 0 :
#         return lst[k][n]
#     else :
#         sol = 0
#         for i in range(1, n+1) :
#             sol += sum_apt(lst,k-1, i)  
#         return sol

# test_n = int(input())
# for i in range(test_n) :
#     k = int(input())
#     n = int(input())
#     matrix = [[0 for _ in range(n+1)] for _ in range(k+1)]

#     print(sum_apt(matrix, k, n))

test_n = int(input())

for i in range(test_n) :
    k = int(input())
    n = int(input())

    matrix = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for s in range(k) :
        for j in range(1, n + 1) :
            if s == 0 :
                matrix[s][j] = j
            else :
                for l in range(j+1) :
                    matrix[s][j] += matrix[s-1][l] 
    
    sol = sum(matrix[k-1])
    print(sol)