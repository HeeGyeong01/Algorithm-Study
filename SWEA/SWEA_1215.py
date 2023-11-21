import math
dir_lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def search(r,c):
    global N, lst, result, slst
    
    for d in range(4): #사방 중 한 방향 선택
        pld = [lst[r][c]]
        nr, nc = r, c
        dr, dc = dir_lst[d]
        for n in range(1, N): #회문 길이만큼 쭉 감       
            nr, nc = nr+dr, nc+dc
            if 0 <= nr < 8 and 0 <= nc < 8: # 평면판 범위 안에서 이동하는 경우
                pld.append(lst[nr][nc])
                if len(pld) >= (math.ceil(N/2)+1): #회문 판단할 수 있을 만큼 길어졌을 때        
                    if pld[-1] != pld[N-n-1]: #회문이 아닌경우 중단함
                        break
                
                if n == N-1:
                    result +=1
                                       
            else: # 평면판 범위 밖으로 넘어가는 경우
                break    


for tc in range(1, 11):
    N = int(input())
    slst = set([])
    lst = []
    result = 0   
    
    if N == 1:
        result = 64
    else:        
        for _ in range(8):
            lst.append(list(input()))
            
        for i in range(8):
            for j in range(8):
                search(i, j)   
    
    print(f'#{tc} {result//2}')