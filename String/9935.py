import sys

input = sys.stdin.readline


def main():
    # s1 = "mirkovC4nizCC44"
    # explode = "C4"
    # s1 = "12ab112ab2ab"
    # explode = "12ab"
    s1 = input().rstrip()
    explode = input().rstrip()
    s_len = len(s1)
    ex_len = len(explode)
    stk = []
    for i in range(s_len):
        stk.append(s1[i])
        while stk:
            tmp = "".join(stk[-ex_len:])
            if tmp == explode:
                for _ in range(ex_len):
                    stk.pop()
            else:
                break
    if len(stk) == 0:
        print("FRULA")
    else:
        print("".join(stk))


main()
