def main():
    #       a, b ,c ,d ,e ,f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    # num = [ 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 ]
    # a = input()
    # b = input()
    # result = a + b
    # list = []
    # for i in result:
    #     list.append(num[ord(i) - 65])
    # while len(list) != 2:
    #     size = len(list)
    #     for i in range(size):
    #         if i == size - 1:
    #             list.pop(0)
    #             break
    #         now = list[0]
    #         list.pop(0)
    #         next = list[0]            
    #         sum = now + next
    #         if sum >= 10:
    #             sum = sum % 10
    #         list.append(sum)
    # print(str(list[0])+str(list[1]))
    alpha = '32123323322122122212111221'
    a = input()
    b = input()
    s = []
    for i in range(len(a)):
        s.append(int(alpha[ord(a[i])-65]))
        s.append(int(alpha[ord(b[i])-65]))
        
    # print(s)
    for i in range(len(a)+len(b)-1, 1, -1):
        ss = []
        for j in range(i):
            ss.append((s[j]+s[j+1])%10)
        s = ss
        # print(s)
    print(str(s[0])+str(s[1]))
        
    
    
if __name__=="__main__":
    main()