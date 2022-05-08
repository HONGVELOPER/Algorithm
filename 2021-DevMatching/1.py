def solution(rows, columns, queries):
    answer = []
    li = [[0] * (columns) for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            li[i][j] = cnt
            cnt += 1

    def turn(query):
        ax, ay = query[0] - 1, query[1] - 1
        bx, by = query[2] - 1, query[3] - 1
        length = (bx - ax + 1) * (by - ay + 1) - ((bx - ax - 1) * (by - ay - 1))
        now = [ax, ay]  # 현재 위치
        pvt = li[now[0]][now[1]]  # 덮여지기 전에 저장해놓은 값
        sm = []
        for _ in range(length):
            if now[1] + 1 <= by and now[0] == ax:
                now[1] = now[1] + 1
            elif now[0] + 1 <= bx and now[1] == by:
                now[0] = now[0] + 1
            elif now[1] - 1 >= ay:
                now[1] = now[1] - 1
            elif now[0] - 1 >= ax:
                now[0] = now[0] - 1
            tmp = li[now[0]][now[1]]
            sm.append(pvt)
            li[now[0]][now[1]] = pvt
            pvt = tmp
        answer.append(min(sm))

    for i in queries:
        turn(i)
    return answer


# solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
# solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
solution(100, 97, [[1, 1, 100, 97]])
