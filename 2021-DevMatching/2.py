def solution(enroll, referral, seller, amount):
    # enroll :판매원 이름
    # referral : 각 판매원을 다단계 조직에 참여시킨 다른 판매원
    # seller : 판매량 집계 데이터의 판매원 이름
    # amount : 판매 수량
    answer = [0] * len(enroll)
    en = {}
    for i, val in enumerate(enroll):
        en[val] = i
    for i, val in enumerate(seller):
        my_money = amount[i] * 100  # i가 팔은 돈
        ref_money = my_money // 10
        my_money -= ref_money
        ref_id = en[val]
        answer[ref_id] += my_money
        print("while~~~~~~~~", val)
        while True:
            print("id : ", ref_id, " name : ", referral[ref_id])
            ref_val = referral[ref_id]
            if ref_val != "-":
                ref_id = en[ref_val]
            else:
                print(answer)
                break
            answer[ref_id] += ref_money - (ref_money // 10)
            ref_money //= 10
            if ref_money == 0:
                break
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll, referral, seller, amount)
