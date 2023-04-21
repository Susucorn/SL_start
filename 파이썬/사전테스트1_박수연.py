'''
2023.04.21
박수연
놀이공원 입장료 계산 프로그램 작성하기

#문제분석
    변수 - 어린이 인원수(num1), 보통 인원수(num2), 경로우대 인원 수 (num3)
            총 어린이 요금(total1), 총 보통 요금(total2), 총 경로우대 요금(total3) , 총 지불해야 할 입장료(total)
    수식 - total1 = 5000*num1, total2 = 10000*num2, total3 = 7000*num3
            total = total1 + total2 + total3
            num1+num2+num3>=10 일때 total * 0.2 (10인 이상일 때)
    논리 조건 (if else)
'''

num1 = int(input('어린이 요금은 몇 명인지 입력하세요 : ')) # 정수로 입력받기
num2 = int(input('보통 요금은 몇 명인지 입력하세요 : ')) # 정수로 입력받기
num3 = int(input('경로우대 요금은 몇 명인지 입력하세요 : ')) # 정수로 입력받기

total1 = (5000*num1) # 총 어린이 요금
total2 = (10000*num2) # 총 보통 요금
total3 = (7000*num3) # 총 경로우대 요금

total = total1 + total2 + total3 # 총 입장료

if num1+num2+num3>=10:
    print('총 입장료는 {} 원 입니다.'.format(total*0.2))
else:
    print('총 입장료는 {} 원 입니다.'.format(total))

