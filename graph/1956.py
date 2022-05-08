import sys
input = sys.stdin.readline
INF = sys.maxsize
def main():
    # v = 3
    # e = 4
    # graph = [
    #     [1000, 1000, 1000, 1000],
    #     [1000, 1000, 1, 5],
    #     [1000, 1000, 1000, 2],
    #     [1000, 1000, 1, 1000]
    # ]
    v, e = map(int, input().split())
    graph = [[INF] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    def floyd():
        for k in range(1, v+1): #! 거쳐가는 노드
            for i in range(1, v+1): #! 출발 노드
                for j in range(1, v+1): #! 도착 노드
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    for a in graph[1:]:
                        print(a[1:])
                    print("========================")
    floyd()
    ans = INF
    for i in range(1, v+1):
        ans = min(ans, graph[i][i])
    if ans == INF:
        print(-1)
    else:
        print(ans)
main()