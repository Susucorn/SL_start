'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    랜덤으로 10명의 학생의 키와 몸무게 생성하여 파일에 저장하는 프로그램
'''
import random

f_name = list("김이박차성전남소조홍서")
s_name = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(10):
        name = random.choice(f_name) + random.choice(s_name) + random.choice(s_name)    # f_name 에 있는 것중에 하나, s_name 에 있는 것중에 하나, s_name 에 있는 것중에 하나
        weight = random.randrange(40,100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {} \n".format(name, weight, height))