'''
2023.04.21
박수연
인치를 입력받아 센티미터로 변환하는 프로그램 작성

# 문제분석
    변수 - 인치(inch)
    수식 - inch * 2.54

# 알고리즘
    1. 변수 지정 (실수값으로 받기)
    2. inch * 2.54 결과 출력
'''

inch=float(input('인치를 입력하세요 : ')) # 인치값은 실수값으로 받기
print(inch*2.54,'cm') # 센티미터로 변환