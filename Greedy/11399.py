def solve():
    num = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # arr = []
    for i in range(1, len(a)):
        # if i == 0: => 범위를 1부터 시작하여 if 문을 사용하지 않도록 함.
        #     arr.append(a[i])
        # else: 
        # arr.append(arr[i-1] + a[i])
        a[i] += a[i-1] # => 새로운 리스트가 아닌 현재 리스트의 값을 바꾸게 함.
    print(a)
    print(sum(a))
solve()