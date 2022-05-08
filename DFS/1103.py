import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def main():
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(input()))
    visited = [[0] * m for _ in range(n)]
    cache = [[1] * m for _ in range(n)]

    def dfs(row, col, count):
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move = int(board[row][col])
        for dx, dy in direction:
            nx = row + dx * move
            ny = col + dy * move
            if (
                0 <= nx < n
                and 0 <= ny < m
                and board[nx][ny] != "H"
                and cache[nx][ny] < count + 1
            ):
                if visited[nx][ny]:
                    print(-1)
                    exit()
                visited[nx][ny] = True
                cache[nx][ny] = max(cache[nx][ny], count + 1)
                dfs(nx, ny, count + 1)
                visited[nx][ny] = False

    dfs(0, 0, 1)
    result = 1
    for i in range(n):
        for j in range(m):
            result = max(result, cache[i][j])
    print(result)


main()
