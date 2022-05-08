import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    kk = k
    num = list(input().rstrip())
    # 4 / 2 / 1924
    result = []

    for i in range(n):  #! 반복문을 돌면서
        print("i : ", i)
        while k and result:  #! k와 result 모두에 값이 있을경우 (초기는 result 가 없음)
            print(result[-1], " / ", num[i])
            if result[-1] < num[i]:  #! result에 최근 들어온 값보다 현재값이 더 큰 경우
                result.pop()  #! result 최근 값 제거
                k -= 1  #! 제거 가능 횟수 1개 줄이기
            else:
                break  #! result 최근 값이 더 큰 경우
        result.append(num[i])  #! result에 값 추가
        # print("result : ", result, "  num[i] :", num[i])

    for i in range(n - kk):
        print(result[i], end="")

    # def find_big(k):
    #     global s
    #     print(stack, k)
    #     if k > 0:
    #         mx = (0, 0)
    #         for i in range(k + 1):
    #             if mx[1] < int(stack[i]):
    #                 mx  = (i, int(stack[i]))
    #         # print("mx : ", mx)
    #         k -= mx[0]
    #         for i in range(mx[0]):
    #             stack.popleft()
    #         mx = stack.popleft()
    #         s += mx
    #         # print(mx)
    #         find_big(k)
    #     else:
    #         for i in stack:
    #             s += i
    #         print("s :", s)
    #         # 값 출력하는 것

    # find_big(k)


main()
