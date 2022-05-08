import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def main():
    # pre_order = []
    # count = 0
    # while count <= 10000:
    #     try:
    #         temp = int(input())
    #     except:
    #         break
    #     pre_order.append(temp)
    #     count += 1
    pre_order = [50, 30, 24, 5, 28, 45, 98, 52, 60]

    def post_order(start, end):
        print("==================")
        if start > end:
            print("Start :", start, " / End : ", end)
            return
        root = pre_order[start]
        id = start + 1

        while id <= end:
            if pre_order[id] > root:
                break
            id += 1

            print("id : ", id)
        post_order(start + 1, id - 1)
        post_order(id, end)
        print(root)

    post_order(0, len(pre_order) - 1)


main()
