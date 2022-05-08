def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        li = []
        for _ in range(h):
            li.append(list(map(int, input().split())))
        visited = [[0] * w for _ in range(h)]

        def dfs(x, y):
            visited[x][y] = 1
            dx = [1, -1, 0, 0, 1, 1, -1, -1]
            dy = [0, 0, 1, -1, 1, -1, 1, -1]
            
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and li[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx, ny)

        count = 0
        for i in range(len(li)):
            for j in range(len(li[i])):
                if li[i][j] == 1 and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)
        print(count)
main()