def main():
    n = input()
    val = []
    sign = []
    num = ''
    for i in n:
        if i.isdigit():
            num += i 
        else:
            val.append(int(num))
            sign.append(i)
            num = ''
    val.append(int(num))
    for i in range(len(sign)):
        if sign[i] == '-':
            val[i+1] = -val[i+1]
            for j in range(i+1, len(sign)):
                if sign[j] == '+':
                    val[j+1] = -val[j+1]
                else:
                    break
    print(sum(val))
main()