import sys

input = sys.stdin.readline
INF = sys.maxsize
import heapq


def main():
    n, e = map(int, input().split())
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())  # a 와 b 양뱡향 / 값 c
        graph[a].append((c, b))
    v1, v2 = map(int, input().split())
    heap = []

    def dijkstra(start):
        dp = [INF] * (n + 1)
        dp[start] = 0
        heapq.heappush(heap, (0, start))
        while heap:
            wei, now = heapq.heappop(heap)  # (0, 1)
            if dp[now] < wei:
                continue
            for w, next_node in graph[now]:
                next_wei = w + wei
                if next_wei < dp[next_node]:
                    dp[next_node] = next_wei
                    heapq.heappush(heap, (next_wei, next_node))
        return dp

    a = dijkstra(1)
    b = dijkstra(v1)
    c = dijkstra(v2)
    print(min(a[v1] + b[v2] + c[n], a[v2] + c[v1] + b[n]))


main()
