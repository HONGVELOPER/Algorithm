from operator import index


def solve():
    
    tt = list(range(1, 10001))
    # def d(n):
    #     con = n
    #     arr = list(map(int, str(n)))
    #     con += sum(arr)
    #     return con
    for i in range(1, 10001):
        d = i
        d += sum(list(map(int, str(i))))
        # a = d(i)
        if d <= 10000:
            print(d)
            tt[tt.index(d)] = -1
            if not tt.index(d):
                continue
    print(tt)
    # for i in tt:
    #     if i != -1:
    #         print(i)
solve()


// set 자료형과 2개의 생성자를 갖는 경우 -1 을 하게 되면 list에서 해당 index를
// 찾을 수 없기 때문에 에러가 발생한다. 다시 생각해보자