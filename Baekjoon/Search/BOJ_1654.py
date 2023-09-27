import sys

n, m = map(int, input().split())
ipt_lst = [int(sys.stdin.readline()) for _ in range(n)]

# 이진탐색
start = 1
end = max(ipt_lst)
result = 0

while start <= end:
    mid = (start + end) // 2

    if m <= sum([x // mid for x in ipt_lst]):  # arr[mid] 길이로 잘랐을 때 나오는 랜선 개수.
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)