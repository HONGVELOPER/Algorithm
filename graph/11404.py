import sys
input = sys.stdin.readline
INF = sys.maxsize
def main():
    # n = 5
    # m = 14
    # graph = [
    #     [1000, 1000, 1000, 1000, 1000, 1000],
    #     [1000, 1000, 2, 3, 1, 10],
    #     [1000, 1000, 1000, 1000, 2, 1000],
    #     [1000, 8, 1000, 1000, 1, 1],
    #     [1000, 1000, 1000, 1000, 1000, 3],
    #     [1000, 7, 4, 1000, 1000, 1000]
    # ]
    n = int(input()) #! 도시의 개수
    m = int(input()) #! 버스의 개수
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        if graph[u][v] > w:
            graph[u][v] = w
    def floyd():
        dist = graph
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j :
                        dist[i][j] = 0
                    else:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
    d = floyd()
    for i in d[:]:
        for j in i[:]:
            if j == 1000:
                print(0, end=' ')
            else:
                print(j, end=' ')
        print()
main()