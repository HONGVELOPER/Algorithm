import re


def main():
    s = input()
    li = []
    for i in range(len(s)):
        li.append(s[i])
    li.sort(reverse=True)
    print(''.join(li))
main()