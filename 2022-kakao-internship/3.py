#! 알고력 코딩력이 다음 풀 수 잇는 문제보다
# 가중치는 1이고 현재 노드 머물시 알고, 코딩 reward , -> bfs ->
import math


def solution(alp, cop, problems):
    last_alp = problems[0][0]
    last_cop = problems[0][1]
    can_solve = []
    answer = 0
    problems = sorted(problems, key=lambda x: ((x[2] + x[3]) / x[4], x[0], x[1]))
    for problem in problems:
        if problem[0] > last_alp:
            last_alp = problem[0]
        if problem[1] > last_cop:
            last_cop = problem[1]
        if problem[0] <= alp and problem[1] <= cop:
            can_solve.append(problem)
    can_solve = sorted(can_solve, key=lambda x: ((x[2] + x[3]) / x[4], x[0], x[1]))
    can_solve = can_solve[-1]
    index = problems.index(can_solve)
    problems = problems[index + 1 :]  # 현재 제일 효율좋은 문제
    while problems:
        print(problems[0][0], problems[0][1], alp, cop)
        if can_solve[2] == 0:
            tmp1 = problems[0][0] - alp
        elif problems[0][0] - alp == 0:
            tmp1 = 0
        else:
            tmp1 = math.ceil(
                (problems[0][0] - alp) / can_solve[2]
            )  # 다음 문제까지 걸리는 alp 횟수 # 2

        if can_solve[3] == 0:
            tmp2 = problems[0][1] - cop
        elif problems[0][1] - cop == 0:
            tmp2 = 0
        else:
            tmp2 = math.ceil(
                (problems[0][1] - cop) / can_solve[3]
            )  # 다음 문제까지 걸리는 cop 효율 # 3
        min_alpcop = min(tmp1, tmp2)  # 한가지를 만족하는 최소 회수
        plus = 0
        if min_alpcop == tmp1:
            plus += 1
        a = can_solve[4] * min_alpcop  # 문제 푼 횟수
        b = problems[0][0 + plus] - (min_alpcop * can_solve[2 + plus])  # 독학
        print("!", a, b)
        set1 = a + b
        set2 = can_solve[4] * max(tmp1, tmp2)  # 3
        print("set ", set1, set2)
        set = min(set1, set2)
        answer += set
        # set1이 min 일 경우
        if set == set1:
            alp = can_solve[0]
            cop = can_solve[1]
        # set2 일 경우
        else:
            if plus == 1:
                alp = problems[0][0]
                cop += can_solve[1] * tmp1
            else:
                alp += can_solve[0] * tmp2
                cop = problems[0][1]
        can_solve = problems[0]
        problems = problems[1:]
    return answer


# solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4], [10, 10, 3, 1, 4]])
print(
    solution(
        0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
    )
)
