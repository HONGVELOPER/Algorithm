import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    li = [[0, 0]]
    for i in range(n):
        li.append(list(map(int, input().split())))  # 4[무게, 가치]
    # n = 4
    # k = 7
    # li = [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):  # 아이템 반복
        wei = li[i][0]
        val = li[i][1]
        for j in range(1, k + 1):  # 무게 반복
            if j < wei:  # 가방에 안들어간다면
                dp[i][j] = dp[i - 1][j]  # 위에 값 복사
            else:  # 가방에 들어간다면
                dp[i][j] = max(val + dp[i - 1][j - wei], dp[i - 1][j])
                # i번째 아이템의 j 무게까지의 최대 값
                # max(i번쨰 아이템 가치 + wei가 들어가지 않은 무게의 최대값에 따른 최대 가치, 위에 값)
    print(dp[-1][-1])
    for _ in dp:
        print(_)


main()
