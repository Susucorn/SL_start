'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    사용자로부터 정수를 입력받아 1부터 입력 받은 수 까지 369 게임 진행하는 프로그램

# 문제분석
    3, 6, 9에서는 "짝"을
    10, 20, 30... 10의 배수 자리에는 '만세'를 출력하는 부분은 함수로 작성하기
'''
def game(num) : # 지역 변수
    for i in range(1,num+1):
        if i%10==3 or i%10==6 or i%10==9:
            print("짝", end=', ')
        elif i % 10 ==0:
            print("만세", end=", ")
        else:
            print(i, end=', ')

print("<<< 369 게임 >>>")
num = int(input("정수를 입력하세요 : "))
game(num)   # 함수 호출하기

