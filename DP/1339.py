import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = []
    dict = {}
    result = []
    for i in range(n):
        li.append(input().strip())

    for i in range(n):
        for j in range(len(li[i])):
            if li[i][j] in dict:
                dict[li[i][j]] += 10 ** (len(li[i]) - j - 1)
            else:
                dict[li[i][j]] = 10 ** (len(li[i]) - j - 1) 
            # len(li[i]) - j == 단어 총 길이 - 현재 자리수 - 1
            # 예를들어 "ABC"의 길이는 3, J는 2번째 숫자임으로
            # 3 - 1 - 1 = 1
    for val in dict.values():
        result.append(val)

    result.sort(reverse=True)

    sum = 0
    pvt = 9
    for i in result:
        sum += pvt * i
        pvt -= 1
    print(sum)
    


main()





























# import sys
# input = sys.stdin.readline
# def main():
#     # li = ['GCF', 'ACDEB']
#     # li = ['AAA', 'AAA']
#     # li = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     # li.sort(key = lambda x : -len(x))
#     n = int(input())
#     li = []
#     for i in range(n):
#         li.append(input().strip())
#     result = []
#     dict = {}
#     length = 0
#     for i in li:
#         if len(i) > length:
#             length = len(i)
#     pvt = 9
#     for i in li:
#         q = []
#         for _ in range(length - len(i)):
#             q.append(0)
#         for j in i:
#             q.append(j)
#         result.append(q)
#     # print("result : ", result)
#     for i in range(length): #  5
#         for j in range(len(li)): # 2
#             if result[j][i] != 0 and result[j][i] not in dict:
#                 dict[result[j][i]] = pvt
#                 pvt -= 1
#     # print("dict : ", dict)
#     sum = 0
#     for i in result:
#         temp = ''
#         for j in i:
#             if j in dict:
#                 temp += str(dict[j])
#         sum += int(temp)
#     print(sum)
        
# main()