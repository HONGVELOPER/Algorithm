# 포도두 잔을 선택하면 전부 마셔야하며, 마신 후에는 제 위치에 놔야 한다.
# 연속으로 있는 3잔을 마실 수는 없다.
# 가능한 많은 양의 포도주를 마시는 방법
def main():
    # li = [6, 10, 13, 9, 8, 1]
    n = int(input())
    li = [0] * 10000
    for i in range(n):
        li[i] = int(input())
    dp = [0] * 10000
    dp[0] = li[0]
    dp[1] = dp[0] + li[1]
    dp[2] = max(li[2] + li[0], li[2] + li[1])
    for i in range(3, len(li)):
        dp[i] = max(dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i], dp[i-1])
    print(max(dp))
    
    
main()