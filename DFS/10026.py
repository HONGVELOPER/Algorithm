import sys

input = sys.stdin.readline


def main():
n = int(input())
li = []
for i in range(n):
    s = list(input().strip())
    li.append(s)
# print(li)
# n = 5
# li = [
#     ["R", "R", "R", "B", "B"],
#     ["G", "G", "B", "B", "B"],
#     ["B", "B", "B", "R", "R"],
#     ["B", "B", "R", "R", "R"],
#     ["R", "R", "R", "R", "R"],
# ]
visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs1(r, c, char):
    # print("row :", r, "/ col : ", c, " /char : ", char)
    visited1[r][c] = 1
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if (
            0 <= nr < n
            and 0 <= nc < n
            and li[nr][nc] == char
            and not visited1[nr][nc]
        ):
            dfs1(nr, nc, char)

def dfs2(r, c, char):
    # print("row :", r, "/ col : ", c, " /char : ", char)
    visited2[r][c] = 1
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and not visited2[nr][nc]:
            if li[nr][nc] == "G" and char == "R":
                dfs2(nr, nc, li[nr][nc])
            elif li[nr][nc] == "R" and char == "G":
                dfs2(nr, nc, li[nr][nc])
            elif li[nr][nc] == char:
                dfs2(nr, nc, li[nr][nc])

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs1(i, j, li[i][j])
            cnt1 += 1
        if not visited2[i][j]:
            dfs2(i, j, li[i][j])
            cnt2 += 1
print(cnt1, cnt2)


main()
