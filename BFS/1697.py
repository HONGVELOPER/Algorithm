from collections import deque
def main():
    n, k = map(int, input().split())
    max = 100000
    li = [0] * (max + 1)
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(li[a])
            break;
        for j in (a-1, a+1, a*2):
            if 0 <=  j <= max and not li[j]: # li[j] 가 0일때
                li[j] = li[a] + 1
                q.append(j)
    
main()