import heapq
def main():
    n = int(input())
    q = []
    for i in range(n):
        heapq.heappush(q, int(input()))
    if len(q) == 1:
        print(0)
    else:
        count = 0
        while len(q) > 1:
            tmp1 = heapq.heappop(q)
            tmp2 = heapq.heappop(q)
            count += tmp1 + tmp2
            print(q)
            heapq.heappush(q, tmp1 + tmp2)
        print(count)
    print(q)
main()