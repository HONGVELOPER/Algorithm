def main():
    # n = 10
    # k = 4200
    # li = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    n, k = map(int, input().split())
    li = []
    for i in range(n):
        li.append(int(input()))
    li.sort(reverse=True)
    cnt = 0
    for i in li:
        if i > k:
            continue
        cnt += k // i
        k -= (k // i) * i
    print(cnt)
main()