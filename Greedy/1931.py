def solve():
    num = int(input())
    arr = []
    count = 1
    pivot = 0
    for i in range(num):
        arr2 = list(map(int, input().split()))
        arr.append(arr2)
    arr.sort(key = lambda x: x[0])
    arr.sort(key = lambda x: x[1])
    for i in range(1, len(arr)):
        if arr[pivot][1] <= arr[i][0]:
            count += 1
            pivot = i
    print(count)

solve()