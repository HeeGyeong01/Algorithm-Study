n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# 이진 탐색
start = 1
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    if sum([i if i <= mid else mid for i in arr]) <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)