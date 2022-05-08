def solution(n, k, cmd):
    li = [_ + 1 for _ in range(n)]
    print(li)
    for i in cmd:
        # print(i.spl)
        if i.split()[0] == "U":
            print("U", i.split()[1])
            k -= int(i.split()[1])
        elif i.split()[0] == "D":
            print("D", i.split()[1])
            k += int(i.split()[1])
        elif i.split()[0] == "C":
            print("c")
        else:
            print("z")
        print("k ", k)


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
