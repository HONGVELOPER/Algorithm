import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(int, input().split()))
    m = int(input())
    li2 = list(map(int, input().split()))
    # li = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
    # li2 = [10, 9, -5, 2, 3, 4, 5, -10]
    dict = {}
    for i in li:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for j in range(len(li2)):
        if li2[j] in dict:
            li2[j] = dict[li2[j]]
        else:
            li2[j] = 0
    print(" ".join(str(_) for _ in li2))

main()