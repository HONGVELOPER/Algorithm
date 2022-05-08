import sys
input = sys.stdin.readline
def main():
    # n = 4
    # length = [2, 3, 1]
    # price = [5, 2, 4, 1]
    n = int(input()) # 도시 개수
    length = list(map(int, input().split()))
    price = list(map(int, input().split()))
    total = 0
    sm = price[0]
    for i in range(len(length)):
        if price[i] >= sm: # 최저 주유 가격과 같거나 비쌀경우
            total += sm * length[i] # 최저 주유 가격 * 길이 
        else : # 최저 주문 가격보다 더 싼 주유소를 찾은경우
            sm = price[i] # 최저 주유 가격 변환 
            total += sm * length[i] # 바뀐 가격 * 길이
print(total)
main()