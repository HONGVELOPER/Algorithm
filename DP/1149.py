def main():
    # li = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
    # li = [
    #     [71, 39, 44],
    #     [32, 83, 55],
    #     [51, 37, 63],
    #     [89, 29, 100],
    #     [83, 58, 11], 
    #     [65, 13, 15], 
    #     [47, 25, 29], 
    #     [60, 66, 19]
    # ]
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
    for i in range(1, len(li)):
        li[i][0] = min(li[i-1][1], li[i-1][2]) + li[i][0]
        li[i][1] = min(li[i-1][0], li[i-1][2]) + li[i][1]
        li[i][2] = min(li[i-1][0], li[i-1][1]) + li[i][2]
    print(min(li[len(li)-1]))
main()