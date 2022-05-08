def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        dp = [0] * 100 
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        for i in range(3, 100):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[n-1])
main()


# dp 크기를 n 으로 할 경우 n이 1 혹은 2 일 경우 dp[0], dp[1], do[2] 에서
# index out of range 가 발생함
