# dfs + 백트래킹
from itertools import combinations

def dfs(numbers, n):   
    global result
    if n == turn:
        result = max(result, int(''.join(map(str, numbers))))
        return
    else:        
        comb_lst = combinations(range(0, len(numbers)), 2) #숫자판 중 2개 고르는 조합
        for a, b in comb_lst:
            numbers[a], numbers[b] = numbers[b], numbers[a]
            if dict.get((''.join(map(str, numbers)), n), 1): #딕셔너리에 찾는 값이 없으면 1이 반환됨
                dfs(numbers, n+1)
                dict[(''.join(map(str, numbers)), n)] = 0  #딕셔너리에 찾는 값이 없으면 추가함
            numbers[a], numbers[b] = numbers[b], numbers[a] #원상복구       
                                        
            
            
T = int(input())
for tc in range(1, T+1):
    numbers, turn = input().split()
    numbers = list(map(int, numbers))
    turn = int(turn)
    result = 0
    dict = {}
    
    
    dfs(numbers, 0)                                             
    print(f"#{tc} {result}")