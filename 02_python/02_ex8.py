'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    학생 정보를 사전에 저장하고, 특정 학생의 정보(학번)을 입력하여 학생을 찾는 프로그램

# 알고리즘
    1. 학생 정보를 저장할 사전 만들기 - 빈 사전 생성
    2. 학생 정보 입력 - 사전에 저장하기 (z 키를 누르면 종료 - 무한반복)
    3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한반복)
'''

student = {}        # 빈 리스트 생성

print(":: 학생 정보 입력 ::")
while True:
    studentName = input("학생 이름 입력(종료를 원한다면 z키 입력) : ")
    if studentName=="z":
        break
    studentNum = int(input("학번 입력 : "))
    student[studentName] = studentNum
    


print(":: 학생 정보 검색 ::")
while True:
    name = input("찾고자 하는 학생의 이름을 검색하세요 : ")

    if name=="":
        print("프로그램 종료")
        break
    elif name in student:
        print(student[name])       
    elif not name in student:
        print("학생이 없습니다.")
    else:
        break