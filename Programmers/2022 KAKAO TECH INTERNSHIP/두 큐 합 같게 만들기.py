from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    target = (sum(queue1) + sum(queue2)) // 2
    sum_q1 = sum(q1)

    if max(queue1) > target or max(queue2) > target:
        return -1

    while sum_q1 != target:
        if sum_q1 > target:
            q1_val = q1.popleft()
            # q2.append(q1_val)
            sum_q1 -= q1_val
            answer += 1
        elif sum_q1 < target:
            q2_val = q2.popleft()
            q1.append(q2_val)
            sum_q1 += q2_val
            answer += 1

        if len(q2) == 0:
            break


    if sum_q1 == target:
        return answer
    else:
        return -1