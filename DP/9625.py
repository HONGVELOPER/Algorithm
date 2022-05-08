def solve():
    num = int(input())
    list = [0 for _ in range(num + 1)]
    list[1] = 1
    
    for i in range(2, num + 1):
        list[i] = list[i-1] + list[i -2]
    
    print(list[i], list[i - 1])
solve()