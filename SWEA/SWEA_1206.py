for tc in range(1, 10 + 1):
    n = int(input())
    blocks = list(map(int, input().split()))
    result = 0
 
    for i in range(2, n-2):
        gaps = [blocks[i] - blocks[i-1], blocks[i] - blocks[i-2], blocks[i] - blocks[i+1], blocks[i] - blocks[i+2]]
        gap = min(gaps)
        if gap > 0:
            result += gap
             
    print(f'#{tc} {result}')