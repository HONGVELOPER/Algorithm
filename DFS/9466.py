import sys
input = sys.stdin.readline
result = []
def main():
    global result
    t = int(input())
    for i in range(t):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        visit = [1] + [0] * n
        def dfs(id):
            global result
            visit[id] = True
            cycle.append(id)
            num = li[id]
            if visit[num]:
                if num in cycle:
                    print(cycle[cycle.index(num):])
                    result += cycle[cycle.index(num):]
                    print(result)
                return
            else:
                dfs(num)
                
            
        for i in range(1, n+1): 
            if not visit[i]:
                cycle = []
                dfs(i)
        print(n - len(result))
         
main()