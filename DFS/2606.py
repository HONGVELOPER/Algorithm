def main():
    # li = [
    #     [0, 1, 0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0, 1, 0], 
    #     [0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0]
    # ]
    n = int(input())
    m = int(input())
    li = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        li[a-1][b-1] = li[b-1][a-1] = 1
    visit = [0 for i in range(n)]
    def dfs(c):
        visit[c] = 1
        for i in range(n):
            if li[c][i] == 1 and visit[i] == 0:
                visit[i] = 1
                dfs(i)
    dfs(0)
    print(sum(visit) - 1)
main()