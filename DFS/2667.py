def solve():
    # num = 7
    # map = [
    #     [0, 1, 1, 0, 1, 0, 0],
    #     [0, 1, 1, 0, 1, 0, 1],
    #     [1, 1, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 1, 1, 1],
    #     [0, 1, 0, 0, 0, 0, 0],
    #     [0, 1, 1, 1, 1, 1, 0],
    #     [0, 1, 1, 1, 0, 0, 0],
    # ]
    num = int(input())
    matrix = []
    for _ in range(num):
        matrix.append(list(map(int, input())))
    cnt = 0
    result = []
    visited = [[0] * num for _ in range(num)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    def dfs(x, y):
        global cnt
        cnt += 1
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < num and 0 <= ny < num and visited[nx][ny] != 1 and matrix[nx][ny] == 1:
                dfs(nx, ny)

    for i in range(num):
        for j in range(num):
            if matrix[i][j] == 1 and visited[i][j] != 1:
                dfs(i, j)
                result.append(cnt);
                cnt = 0
    print(len(result))
    for i in sorted(result):
        print(i)
            
solve()