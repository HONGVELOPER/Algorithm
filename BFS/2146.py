import queue
import sys
from collections import deque

input = sys.stdin.readline
cnt = 1
answer = sys.maxsize


def main():
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]
    # n = 10
    # li = [
    #     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    #     [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    #     [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    def bfs(row, col):
        global cnt
        queue = deque()
        queue.append([row, col])
        visited[row][col] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        li[row][col] = cnt
        while queue:
            v = queue.popleft()
            x, y = v[0], v[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and li[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    li[nx][ny] = cnt

    def bfs2(z):
        global answer
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if li[i][j] == z:
                    queue.append([i, j])
                    dist[i][j] = 0

        while queue:
            v = queue.popleft()
            x, y = v[0], v[1]
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if li[nx][ny] > 0 and li[nx][ny] != z:
                        answer = min(answer, dist[x][y])
                        return
                    if li[nx][ny] == 0 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append([nx, ny])

    global cnt
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    for i in range(1, cnt):
        bfs2(i)

    print(answer)


main()
