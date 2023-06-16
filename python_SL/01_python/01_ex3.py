'''
신라대학교 202395016 컴퓨터공학부 박수연

리스트를 만들고, 반복문으로 출력하기
'''

import random

num1 = list(range(1,10))
print("num1 : ", num1)      # 1부터 9까지 출력, 대괄호로 출력

for i in num1:
    print(i, end=', ')      # 1부터 9까지 옆으로 ,로 이어서 출력, 안에 있는 값만 출력

print()

# 1~100 사이의 정수 중 랜덤으로 10개의 수를 뽑아서 리스트(num2)에 저장하기
num2 = []                               # 빈 리스트 생성

for i in range(10):                     # 10번 반복
    num2.append(random.randint(1,100))  # num2에 1부터 100까지 숫자 중에 10개를 추가
print("생성된 리스트 : ", num2)
