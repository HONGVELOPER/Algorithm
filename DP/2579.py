def main():
    li = [10, 20, 15, 25, 10, 20]
    n = int(input())
    dp = []
    li = []
    for _ in range(n):
        li.append(int(input()))
    if n == 1:
        print(li[0])
        return
    elif n == 2:
        print(li[0] + li[1])
        return
    dp.append(li[0])
    dp.append(li[0] + li[1])
    dp.append(max(li[0] + li[2], li[1] + li[2]))
    for i in range(3, n):
        dp.append(max(dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i]))
    print(dp[-1])
main()