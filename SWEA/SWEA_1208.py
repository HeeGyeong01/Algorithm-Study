#간단한 리스트 조작
for tc in range(1, 11):
    turn = int(input())
    lst = list(map(int, input().split()))
    
    for _ in range(turn):
        max_num = max(lst)
        min_num = min(lst)
        
        if max_num - min_num == 0 or max_num - min_num == 1:
            break
            
        lst.remove(max_num)
        lst.remove(min_num)
        
        lst.append(min_num+1)
        lst.append(max_num-1)
    
    result = max(lst) - min(lst)
    print(f"#{tc} {result}")