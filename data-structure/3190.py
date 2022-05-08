import sys

input = sys.stdin.readline


def main():
    # n = int(input())
    # k = int(input())
    # li = [[0] * n for _ in range(n)]
    # for i in range(k):
    #     a, b = map(int, input().split())
    #     li[a][b] = 1

    # l = int(input())
    # dict = {}
    # for i in range(l):
    #     a, b = input().split()
    #     dict[(int(a)] = b
    n = 6
    li = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
    ]
    dict = {3: "D", 15: "L", 17: "D"}
    second = 0
    direct = ["right", "down", "left", "up"]
    now_direct = "right"
    tail = (0, 0)
    for i in range(n):
        for j in range(n):
            second += 1
            if li[i][j] == 1:
                if direct == direct[0]:
                    li[i][j - 1] = 1
                elif direct == direct[1]:
                    li[i - 1][j] = 1
                elif direct == direct[2]:
                    li[i][j + 1] = 1
                elif direct == direct[3]:
                    li[i + 1][j] = 1
            else:
                li[i][j] = 1
                li[tail[0], tail[1]] = 0
            if second in dict:
                turn(now_direct, dict[second])

    def turn(now_direct, degree):
        if degree == "D":
            now_direct = direct[direct.index(now_direct) + 1] % 4
        elif degree == "L":
            now_direct = direct[direct.index(now_direct) - 1] % 4


main()
