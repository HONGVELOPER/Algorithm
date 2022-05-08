import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
def main():
    n, m, x = map(int, input().split()) # n : 노드 수 / m : 간선의 수 / x : dest
    graph = [[] for _ in range(n+1)] 
    q = []
    def dijksta(start):
        distance = [INF] * (n+1)
        distance[start] = 0
        heapq.heappush(q, (0, start))
        while q:
            wei, now_dest = heapq.heappop(q)
            # print("wei : ", wei, " / now : ", now_dest)
            if distance[now_dest] < wei:
                continue
            for w, next_node in graph[now_dest]:
                next_wei = w + wei
                if next_wei < distance[next_node]:
                    distance[next_node] = next_wei
                    heapq.heappush(q, (next_wei, next_node))
                    # print(" q : ", q)
                    
            # print("dis :", distance)
        return distance
    for _ in range(m):
        v, d, w = map(int, input().split())
        graph[v].append((w, d))
    print(graph)
    # graph = [[], [(4, 2), (2, 3), (7, 4)], [(1, 1), (5, 3)], [(2, 1), (4, 4)], [(3, 2)]]
    ans = [0] * (n + 1)
    for i in range(1, n+1):
        dist = dijksta(i)
        print("dist1 : ", dist)
        ans[i] += dist[x]
        print(ans, "ans 1 check")
        dist = dijksta(x)
        print("dist2 : ", dist)
        ans[i] += dist[i]
        print(ans, "ans 2 check")
    print("ans : ", max(ans))
main()