import sys
input = sys.stdin.readline
def main():
    # n = 4
    # li = [0, 3, 5, 15, 16]
    n = int(input())
    li =  [0] + list(map(int, input().split()))
    dp = [0] * (n+1)
    dp[1] = li[1]
    for i in range(2, n+1):
        for j in range(1, i + 1):
            if dp[i] < dp[i - j] + li[j]:
                dp[i] = dp[i - j] + li[j]       
    print(dp[-1])
    
    
main()

#! 개당 가격이 비싸고, 나누어 떨어지는 것
#! 나누어 떨어지지 않으면 비싼 순서대로,
#! dp 배열에는 n개를 사기 위해 드는 최대 금액.

# dp = [3]
# dp = [3, 6]
# dp = [3, 6, 15]
# dp = [3, 6, 15, 18]