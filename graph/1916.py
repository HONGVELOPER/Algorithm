import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def main():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
    print(graph)
    start, end = map(int, input().split())
    dp = [INF for _ in range(n + 1)]
    q = []

    def dijkstra(start):
        dp[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            wei, now = heapq.heappop(q)
            if dp[now] < wei:
                continue
            for w, next_node in graph[now]:
                next_wei = wei + w
                if next_wei < dp[next_node]:
                    dp[next_node] = next_wei
                    heapq.heappush(q, (next_wei, next_node))

    dijkstra(start)
    print(dp[end])


main()
