'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    학생 관리 프로그램 작성하기

# 문제분석
    이 프로그램은 종료 시킬 때까지 무한반복 되게하기
    - "작업 선택 : " 에서 0 입력 시 프로그램이 종료됨
    - "작업 선택 : " 에서 1 입력 시 관리하는 학생 목록이 조회됨
    - "작업 선택 : " 에서 2 입력 시 학생을 추가함
    - "작업 선택 : " 에서 3 입력 시 학생을 삭제함

    이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며 목록에 없는 학생을 삭제하고자 할 때는
    "삭제 할 학생이 없습니다. 다시 입력하세요" 를 화면에 출력
'''

student = []    # 이름을 저장할 빈 리스트 생성
i = 1
num = int(input("학생 수 입력 : "))

while i<=num:  
    name = input("학생 이름 : ")
    student.append([name])  # 이름을 리스트에 추가하기
    i+=1

print("::: 학생 관리 프로그램 :::")
print("작업 선택 0. 종료")
print("작업 선택 1. 학생 조회")
print("작업 선택 2. 학생 추가")
print("작업 선택 3. 학생 삭제")
print("==========================")



while True:
    work = int(input("작업을 선택하세요 : "))
    
    if work==0:
        break
    elif work==1:
        print(student)
    elif work==2:
        name2 = input("새로 추가할 학생의 이름을 입력하세요 (추가할 학생이 없다면 4를 입력) : ")
        student.append([name, name2])
        if name2!="4":
            continue
    elif work==3:
        name3 = input("삭제할 학생의 이름을 입력하세요 : ")
        student.remove([name3])
    else:
        break

    