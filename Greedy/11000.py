import sys
import heapq

input = sys.stdin.readline


def main():
    # n = 3
    # time = [[1, 3], [2, 4], [3, 5]]
    n = int(input())
    time = []
    for _ in range(n):
        time.append(list(map(int, input().split())))
    time.sort(key=lambda x: (x[0], x[1]))
    heap = []
    heapq.heappush(heap, time[0][1])
    for i in range(1, n):
        if time[i][0] < heap[0]:  #! 수업이 안끝낫는데 다른 수업이 시작할경우
            heapq.heappush(heap, time[i][1])
        else:
            heapq.heappop(heap)  #! 수업이 끝나고 다른 수업이 시작할경우
            heapq.heappush(heap, time[i][1])
    print(len(heap))


main()
