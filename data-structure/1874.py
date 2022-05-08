def main():
    n = int(input())
    stack = []
    cnt = 0
    li = []
    result = True
    for i in range(n):
        a = int(input())
        while cnt < a:
            cnt += 1
            stack.append(cnt)
            li.append('+')
        if stack[-1] == a:
            stack.pop()
            li.append('-')
        else:
            result = False
            break
    if not result:
        print('No')
    else:
        for i in li:
            print(i)
main()