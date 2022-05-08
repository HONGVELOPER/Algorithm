import sys
input = sys.stdin.readline
def main():
    n = list(input().strip())
    print(n)
    n.sort(reverse=True)
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0 and '0' in n:
        print(''.join(n))
    else:
        print(-1)
        
main()