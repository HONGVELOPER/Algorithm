def solution():
    time = 0;
    # num, rule = map(int, input().split())
    # arr = list(map(int, input().split()))
    # load = []
    # for _ in range(rule):
    #     before, after = map(int, input().split())
    #     load.append([before, after])
    # dest = int(input())
    num = 4
    rule = 4
    arr = [10, 1, 100, 10]
    load = [[1, 2], [1, 3], [2, 4], [3, 4]]
    dest = 4
    count = [0 for i in range(len(load))]
    for i in range(len(load)):
        count[load[i][1]-1] += 1
    print(count)
solution()