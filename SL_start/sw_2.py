'''
2023.04.21
박수연
시급과 노동 시간을 입력 받아 수당을 계산하는 프로그램 작성

# 문제분석
    변수 - 시급(hou), 시간(time), 수당(money)
    수식 - money = hou * time

# 알고리즘
    1. 변수 지정 (정수 값으로 받기)
    2. 결과 출력
'''

hou=int(input('시급을 입력하세요 : ')) # 시급은 정수값으로 받기
time=int(input('시간을 입력하세요 : ')) # 시간은 정수값으로 받기
money=hou*time # 수당

print('시급 {}원으로 {}시간 일했으므로 수당은 {}원 입니다.'.format(hou,time,money))