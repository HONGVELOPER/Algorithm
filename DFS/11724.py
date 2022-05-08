import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(key):
        print(key)
        visited[key] = 1
        for i in graph[key]:
            if visited[i] == 0:
                dfs(i)
            
    count = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            print("===========")
            dfs(i)
            count += 1
    print("c :", count)
main() 