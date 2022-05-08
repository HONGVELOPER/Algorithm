def solve():
    a = int(input())
    b = list(map(int, input().split()))
    c = []
    for id, val in enumerate(b):
        c.insert(id - val, id + 1)
    print(' '.join(str(d) for d in c))
    
    
solve()