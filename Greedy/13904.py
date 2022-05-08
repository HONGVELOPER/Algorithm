import sys

input = sys.stdin.readline
import heapq


def main():
    n = int(input())
    li = []
    for _ in range(n):
        d, w = map(int, input().split())
        li.append((d, w))
    # n = 7
    # li = [(4, 60), (4, 40), (1, 20), (2, 50), (3, 30), (4, 10), (6, 5)]
    li.sort(key=lambda x: (-x[0], -x[1]))
    heap = []
    val = 0
    for i in range(li[0][0], 0, -1):
        for j in li:
            if j[0] == i:
                heapq.heappush(heap, -j[1])
        if len(heap):
            val -= heapq.heappop(heap)
    print(val)


main()
