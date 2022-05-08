import sys
input = sys.stdin.readline
from collections import deque
def main():
    # col = 2 # 가로 칸 수
    # row = 2 # 세로 칸 수
    # li = [[0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
    # li = [[-1, 1, 0, 0, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, 0, 0, 0, 0]]
    # li = [[1, -1], [-1, 1]]
    col, row = map(int, input().split())
    li = []
    for i in range(row):
        li.append(list(map(int, input().split())))
    queue = deque([])
    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] == 1:
                queue.append([i, j])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and li[nx][ny] == 0:
                queue.append([nx, ny])
                li[nx][ny] = li[x][y] + 1
        
    mx = 0
    for i in li:
        if 0 in i:
            print(-1)
            exit()
        else:
            if mx < max(i):      
                mx = max(i)
    print(mx-1)
                

main()