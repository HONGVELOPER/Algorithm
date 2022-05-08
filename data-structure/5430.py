import sys

from collections import deque

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        p = input().rstrip()
        n = int(input())
        li = input().rstrip()[1:-1].split(",")
        q = deque(li)

        reverse = 0
        flag = 0
        if n == 0:
            q = []
        for i in p:
            if i == "R":
                reverse += 1
            elif i == "D":
                if len(q) >= 1:  # 현재 q에 값이 있는경우
                    if reverse % 2 == 0:
                        q.popleft()
                    else:
                        q.pop()
                else:  # 현재 q가 비어있는데 pop 하려고 할떄
                    flag = 1
                    print("error")
                    break
        if flag == 0:
            if reverse % 2 == 0:
                print("[" + ",".join(q) + "]")
            else:
                q.reverse()
                print("[" + ",".join(q) + "]")


main()
