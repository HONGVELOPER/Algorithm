from operator import truediv
import sys
input = sys.stdin.readline
def main():
    # row, col = map(int, input().split())
    # li = []
    # for i in range(row):
    #     li.append(list(map(int, input().split())))
    row = 7
    col = 7
    li = [
        [2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    visited = [[0] * col for i in range(row)]
    print(visited)
    mx = []
    def dfs(x, y):
        visited[x][y] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        direction = 0
        for i in range(4):
            if direction == 2:
                print("==========")
                mx.append([x, y])
                break
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and li[nx][ny] == 0 and visited[nx][ny] == 0:
                dfs(nx, ny)
                li[nx][ny] = 2
                direction += 1

    for i in range(row):
        for j in range(col):
            if li[i][j] == 2:
                dfs(i, j)
                print("진입")
    cnt = 0
    for i in range(len(li)):
        cnt += li[i].count(0)
    print(cnt)
    for i in li:
        print(i)
main()