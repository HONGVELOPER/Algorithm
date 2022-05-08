def solve():
    kg = int(input())
    count = 0
    while kg >= 0:
        if kg % 5 == 0:
            count += (kg // 5)
            print(count)
            break
        kg -= 3 
        count += 1
    else:
        print(-1)
        count = -1

solve()