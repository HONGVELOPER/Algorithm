def main():
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
    li.reverse()
    # li = [[4, 5, 2, 6, 5], [2, 7, 4, 4], [8, 1, 0], [3, 8], [7]]
    for i in range(1, len(li)):
        for j in range(len(li[i])):
            li[i][j] = max(li[i-1][j], li[i-1][j+1]) + li[i][j]
    print(li[-1][0])
main()