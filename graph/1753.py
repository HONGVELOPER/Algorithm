import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
def main():
    V, e = map(int, input().split())
    k = int(input()) #! 시작점
    dp = [INF] * (V + 1) #! 가중치 테이블
    heap = []
    graph = [[] for _ in range(V+1)]
    def dijkstra(start):
        dp[start] = 0
        heapq.heappush(heap, (0, start))
        while heap:
            wei, now = heapq.heappop(heap)
            # print("wei : ", wei, " / now : ", now)
            if dp[now] < wei:
                continue
            for w, next_node in graph[now]:
                next_wei = w + wei
                if next_wei < dp[next_node]:
                    dp[next_node] = next_wei
                    heapq.heappush(heap, (next_wei, next_node))
                    # print(dp)
    for _ in range(e):
        u, v, w = map(int, input().split()) 
        #(가중치, 목적지 노드) 형태로 저장 
        graph[u].append((w, v))
    # print(graph)
    dijkstra(k)
    for i in range(1,V+1):
        print("INF" if dp[i] == INF else dp[i])

main()



# 다익스트라 알고리즘 이용한 최소 경로 구하기
#? 다익스트라 : 시작점으로 부터 나머지 정점까지 최단거리를 구할 때
#? 플로이드 워셜: 각 정점간 최단경로를 구할 때