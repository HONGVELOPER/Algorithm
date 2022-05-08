import sys
input = sys.stdin.readline
def main():
    # n = 10
    # li = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
    n = int(input())
    li = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = li[0]
    for i in range(1, len(li)):
        dp[i] = max(li[i], dp[i-1] + li[i])
    print(max(dp))
main()