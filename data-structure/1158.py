import sys
input = sys.stdin.readline
from collections import deque
def main():
    res = []
    n, k = map(int, input().split())
    li = deque()
    for i in range(n):
        li.append(i+1)
    while len(li) > 1:
        for i in range(k-1):
            a = li.popleft()
            li.append(a)
        res.append(li.popleft())
    res.append(li[0])
    print("<", ", ".join(str(s) for s in res), ">", sep='')
        
main()