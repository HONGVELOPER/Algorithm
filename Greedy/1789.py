import sys
input = sys.stdin.readline
def main():
    s = int(input())
    sum = 0
    cnt = 0
    while sum <= s:
        print("sum :", sum, " / cnt :", cnt)
        sum += cnt
        cnt += 1
    print(cnt-2)
main()