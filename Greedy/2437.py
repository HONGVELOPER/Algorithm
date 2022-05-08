import sys

input = sys.stdin.readline


def main():
    # n = 7
    # weight = [3, 1, 6, 2, 7, 30, 1]
    n = int(input())
    weight = list(map(int, input().split()))
    weight.sort()
    target = 1
    for num in weight:
        if target < num:
            break
        target += num
    print(target)


main()
