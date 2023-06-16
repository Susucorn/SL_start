'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    학생 이름과 점수를 입력 받아 리스트에 저장하고, 학생 점수의 총점과 평균을 출력하시오

# 알고리즘
    0. 빈 리스트 생성
    1. 학생 수 입력받기
    2. 학생 수 만큼 반복하면서
        학생 이름과 점수 저장하기 - 리스트
        점수 합계 계산
    3. 리스트에 저장된 학생 정보 출력
    4. 총점과 평균 출력
'''

student = []    # 빈 리스트 생성
sum = 0         # 합계 저장할 변수 0으로 초기화

num = int(input("학생 수를 입력하세요 : "))                     # 학생 수 입력받기

for i in range(num):                                          # 입력 받은 학생 수 만큼 반복
    print("<", i+1, "번째 학생 정보 입력 >")
    name = input("학생 이름을 입력하세요 : ")                   # 이름 입력받기
    score = int(input("%s 학생의 점수를 입력하세요 : "%name))   # %s는 str 문자열이라는 뜻
    student.append([name, score])                             # student에 name과 score 값을 추가
    sum = sum+score                                           # 점수의 합 저장

for info in student:
    print("이름 : ", info[0], "점수 : ", info[1])  # student에 있는 값을 info 변수에 넣기 - info에 있는 0번째 값은 이름, 1번째 값은 점수

print("학생 점수의 합계 : ", sum)
print("학생 점수 평균 : {:2f}".format(sum/num))     # 소수 둘째자리 까지 출력