def solve():
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(a, a % b)
    num = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, num):
        res = gcd(arr[0], arr[i])
        c = arr[0] // res
        d = arr[i] // res
        print(f"{c}/{d}")
solve()