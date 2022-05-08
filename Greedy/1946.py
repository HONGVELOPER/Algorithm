# 다른 모든 지원자와 비교해서 서류 성적, 면접 성적중 적어도 한개가 다른 지원자보다 깉거나 높다
import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        li = []
        for i in range(n):
            a, b = map(int, input().split())
            li.append((a, b))
        li.sort()
        pvt = li[0][1]
        cnt = 1
        for i in range(1, len(li)):
            if li[i][1] < pvt:
                pvt = li[i][1]
                cnt += 1
        print(cnt)
main()