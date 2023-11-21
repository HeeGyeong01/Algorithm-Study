for tc in range(1, 11):
    input()
    lst = []
    result = 0
    
    for _ in range(100):
        lst.append(list(map(int, input().split())))
    
    #가로합
    for sub in lst:
        result = max(result, sum(sub))
    
    #세로합
    column_sum = [0] * 100
    for i in range(100):
        for j in range(100):
            column_sum[j] += lst[i][j]
    result = max(result, max(column_sum))
    
    #대각선합
    left = 0
    right = 0
    for i in range(100):
        left += lst[i][i]
        right += lst[i][99-i]      
    result = max(result, left, right)
    
    
    print(f'#{tc} {result}')