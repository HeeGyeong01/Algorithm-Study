#너무 어렵게 풀음
#십진수로 바꾸지 않고 문자열("0110111")끼리 비교해도 됐었음

decode = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    
    target_line = 0
    end_idx = 0
    for idx, sub_lst in enumerate(lst):
        if len(str(sub_lst[0])) != 1: #0만 있는 줄이 아닌 경우
            target_line = idx
            break
        
    target_line = list(str(lst[target_line][0]))
    target_line = ['0','0','0'] + target_line

    for idx, x in enumerate(target_line):
        end_idx = idx if x == '1' else end_idx #그 줄에서 맨 오른쪽에 있는 1의 인덱스 찾음
            
    start_idx = end_idx-55
    result = 0
    result_lst = []
    
    
    for i in range(start_idx, end_idx+1, 7):
        num = int(''.join(target_line[i:i+7]), 2) # '0110101'같은 2진수를 10진수로 바꿈.
        decode_num = [idx for idx, x in enumerate(decode) if x == num]
        if (i - start_idx) % 2 == 0: #홀수 자리인 경우
            result += decode_num[0] * 3
            result_lst.append(decode_num[0])
        else: #짝수 자리인 경우
            result += decode_num[0]   
            result_lst.append(decode_num[0])
    
    result = sum(result_lst) if result % 10 == 0 else 0
 
    print(f'#{tc} {result}')