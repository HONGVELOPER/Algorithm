import sys

input = sys.stdin.readline


def main():
    # s1 = "ABRACADABRA"
    # s2 = "ECADADABRBCRDARA"
    # s1 = "UPWJCIRUCAXIIRGL"
    # s2 = "SBQNYBSBZDFNEV"
    s1 = input().rstrip()
    s2 = input().rstrip()
    len1 = len(s1)
    len2 = len(s2)
    result = 0
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    # 앞 글자까지 비교를 통하여 같은 문자를 갖는 개수
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(dp[i][j], result)
    print(result)


main()
