import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for _ in range(t):
        li = []
        n = int(input())
        for _ in range(n):
            li.append(input().strip())
        li.sort()
        result = 'YES'
        for i in range(len(li)-1):
            length = len(li[i])
            if li[i] == li[i+1][:length]:
                result = 'NO'
                break
        print(f'{result}')
main()
# li = ['911', '97625999', '91125426']
# li = ['113','12340','123440','12345','98346']