def main():
    n = int(input())
    dp = [0 for _ in range(n+1)]
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 1  # 2 혹은 3 으로 나누어 떨어지지 않는 경우 1을 빼야함.
        if i % 3 == 0: # 3으로 나누어 떨어지며 dp[i//3] 에 1을 더한 값이 현재 dp[i]보다 작을경우
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0: # 2로 나누어 떨어지며 dp[i//] 에 1을 더한 값이 현재 dp[i]보다 작을경우
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[n])
main()