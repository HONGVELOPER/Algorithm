import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    knowList = set(input().split()[1:])
    parties = []

    for _ in range(m):
        parties.append(set(input().split()[1:]))
    print("knowList :", knowList)
    print("parties ", parties)

    for _ in range(m):
        for party in parties:
            print("=================")
            print("party :", party)
            print("know : ", knowList)
            if party & knowList:  # 교집합이 있다면
                knowList = knowList.union(party)  # 합쳐라
                print("union Know :", knowList)
    cnt = 0
    for party in parties:
        if party & knowList:
            continue
        cnt += 1
    print(cnt)


main()
