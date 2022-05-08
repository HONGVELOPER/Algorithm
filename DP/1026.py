import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
main()

# dp[i]는 li[i]를 마지막 원소르 갖을 때, 가장 긴 증가하는 부분 수열의 길이