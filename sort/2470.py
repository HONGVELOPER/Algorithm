import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    left = 0
    right = n -1
    ans = li[left] + li[right]
    al = left
    ar = right
    while left < right:
        tmp = li[left] + li[right]
        if abs(tmp) < abs(ans):
            ans = tmp
            al = left
            ar = right
            if ans == 0:
                break
        if tmp < 0:
            left += 1
        else:
            right -= 1
    print(li[al], li[ar])
main()


# al, ar 은 절대 값의 차이가 작을 경우에만 바뀜
# left, right 는 비교를 하기 위하여 계속 움직임