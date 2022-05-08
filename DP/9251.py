import sys

input = sys.stdin.readline


def main():
    s1 = input().strip()
    s2 = input().strip()
    # s1 = "ACAYKP"
    # s2 = "CAPCAK"
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:  # s1[i] 와 s2[]j 가 같은 문자일 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 다른 문자일 경우
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[-1][-1])


main()
