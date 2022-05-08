import sys, heapq
input = sys.stdin.readline
INF = 1000
def main():
    count = 0
    while True:
        n = int(input())
        count += 1
        if n == 0:
            break;
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            li = list(map(int, input().split()))
            for j in range(n):
                graph[i][j] = li[j]
        heap = []
        def dijkstra(row, col):
            dist = [[INF] * n for _ in range(n)]
            dist[row][col] = graph[row][col]
            heapq.heappush(heap, (0, 0, graph[0][0]))
            while heap:
                row, col, wei = heapq.heappop(heap)
                # print("wei : ", wei)
                if dist[row][col] < wei:
                    continue
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                for i in range(4):
                    next_row = row + dx[i]
                    next_col = col + dy[i]
                    if 0 <= next_row < n and 0 <= next_col < n:
                        if dist[next_row][next_col] > wei + graph[next_row][next_col]:
                            dist[next_row][next_col] = wei + graph[next_row][next_col]
                            heapq.heappush(heap, (next_row, next_col, wei + graph[next_row][next_col]))
                            # print("dist : ", dist)
            return dist
        d = dijkstra(0, 0)
        print(f"Problem {count}:", d[n-1][n-1])
main()