import sys
input = sys.stdin.readline
def main():
    a = [300, 0]
    b = [60, 0]
    c = [10, 0]
    n = int(input())
    if n % 10 != 0:
        print(-1)
    else:
        while n != 0:
            if n >= a[0]:
                n -= a[0]
                a[1] += 1
            elif n >= b[0]:
                n -= b[0]
                b[1] += 1
            elif n >= c[0]:
                n -= c[0]
                c[1] += 1
        print(a[1], b[1], c[1])
main()