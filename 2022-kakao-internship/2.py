from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    standard = len(q1) + len(q2) + 1
    while sum1 != sum2:
        if answer > standard:
            return -1
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            temp = q1.popleft()
            q2.append(temp)
        else:
            sum1 += q2[0]
            sum2 -= q2[0]
            temp = q2.popleft()
            q1.append(temp)
        answer += 1
    return answer
