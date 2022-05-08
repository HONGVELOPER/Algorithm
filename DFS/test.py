def foo():
    x = 10
    def check():# 전역 변수
        global x    # 전역 변수 x를 사용하겠다고 설정
        x = 20      # x는 전역 변수
    check()
    print(x)    # 전역 변수 출력
foo()
print(x) 