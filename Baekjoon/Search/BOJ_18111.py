# 조건1. 인벤토리 block 수 고려해야 함
# 조건2. 걸리는 시간이 같다면 땅 높이가 가장 높은 것으로 출력할 것
import itertools

n, m, b = map(int, input().split())
min_time = float("inf")
height = 0

arr = [list(map(int, input().split())) for _ in range(n)]
arr = list(itertools.chain.from_iterable(arr))  # 2차원 리스트를 1차원으로 변환(Flatten)

for i in range(min(arr), max(arr) + 1):
    result_arr = [i - x for x in arr]
    # -sum(result_arr) = 인벤토리에 추가되거나 제거되는 블록 수
    block_state = b - sum(result_arr)

    if block_state >= 0:  # 인벤토리의 블록 수가 모자라지 않을 때
        result_arr = [x if x >= 0 else x * -2 for x in result_arr]
        if sum(result_arr) <= min_time:
            min_time = sum(result_arr)
            height = i

print(min_time, height)