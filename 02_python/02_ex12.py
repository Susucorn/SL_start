'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    키와 몸무게로 비만도 계산하기
'''
with open("info.txt","r") as file:
    for line in file:                # strip()공백제거, split(",") 쉼표로 구분
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue
    # 비만도 계산하기
        bmi = (int(weight) / (int(height)/100) ** 2 )   # 텍스트 파일에서 들고오는 값은 문자열, 정수로 바꿔서 계산하기
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "bmi : {:.2f}", "결과 : {}"]).format(name, weight, height, bmi, result))

    