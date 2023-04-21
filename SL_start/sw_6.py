'''
2023.04.21
박수연
년도를 입력받아 윤년인지 아닌지 여부를 판단하는 프로그램 작성

# 문제분석
    변수 - 년도(year)
    논리 (if, elif, else)

# 알고리즘
    1. 변수 지정 (정수값으로 받기)
    2. 논리 (if, elif, else)
        if year이 4로 나누었을때 나머지가 0이면
            윤년 출력
        elif year이 100로 나누었을때 나머지가 0이면
            윤년 아님 출력
        elif year이 400로 나누었을때 나머지가 0이면
            윤년 출력
        else
            윤년 아님 출력
'''

year=int(input('년도를 입력하세요 : ')) #년도는 정수로 입력받기

if year%4==0 and year%400==0:
    print(year,'년은 윤년입니다.')
elif year%100==0:
    print(year,'년은 윤년이 아닙니다.')
else:
    print(year,'년은 윤년이 아닙니다.')
    "코드 수정하기"