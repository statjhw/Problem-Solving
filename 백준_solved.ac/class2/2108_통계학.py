#2108_통계학
#시간 복잡도 : O(nlogn)
import sys 
from collections import defaultdict

input = sys.stdin.readline

class stat :
    def __init__(self) :
        pass

    def mean(self, arr) :
        """음수인 경우도 존재"""
        m = sum(arr) / len(arr)
        return round(m)
    
    def median(self, arr) :
        sorted_arr = sorted(arr)
        idx = len(sorted_arr) // 2
        return sorted_arr[idx]

    def mode(self, arr) :
        if len(arr) == 1 : 
            return arr[0]
        else :
            diction = defaultdict(int)
            for i in arr :
                diction[i] += 1
            
            sorted_value = sorted(diction.items(), key=lambda x : x[1], reverse=True)
        
            
            if sorted_value[0][1] == sorted_value[1][1] :
                mode_value = [x for x in sorted_value if x[1] == sorted_value[0][1]]
                return sorted(mode_value, key=lambda x : x[0])[1][0]
            else :
                return sorted_value[0][0]

    
    def range(self, arr) :
        sorted_arr = sorted(arr)
        return sorted_arr[-1] - sorted_arr[0]


N = int(input())

lst = []

for _ in range(N) :
    lst.append(int(input()))

s = stat()
print(s.mean(lst))
print(s.median(lst))
print(s.mode(lst))
print(s.range(lst))