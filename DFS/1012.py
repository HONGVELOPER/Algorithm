import sys
sys.setrecursionlimit(10000) 
def main():
    # m = 10 # 열
    # n = 6 # 행 
    # k = 17 # 총 배추 수
    # li = [
    #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 1, 0 ,0, 1, 1, 1],
    # ]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    li = [[0] * m for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        li[b][a] = 1
    visited = [[0] * m for i in range(n)]
    cnt = 0
    def dfs(r, c):
        visited[r][c] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < m and li[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr, nc)
                
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)     
                cnt += 1
    print(cnt)
main()