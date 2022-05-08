
import sys
input = sys.stdin.readline
def main():
    dict = {}
    n = int(input())
    li = list(map(int, input().split()))
    m = int(input())
    li2 = list(map(int, input().split()))
    for i in li:
        dict[i] = 1
    for i in li2:
        if i in dict:
            print(1)
        else:
            print(0)

main()