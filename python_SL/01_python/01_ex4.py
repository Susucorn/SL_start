'''
신라대학교 202395016 컴퓨터공학부 박수연

continue

'''

# 리스트의 값 10개 중에서 10보다 큰 수 출력하기
numbers = [3, 44, 12, 6, 29, 93, 4, 32, 10, 52]

print("리스트 값중 10보다 큰 수 - 반복문 사용")

for i in numbers:
    if i >=10:
        print(i, end=', ')

print()

print("리스트 값 중 10보다 큰 수 - continue 사용")

for i in numbers:   # numbers 안에서 반복
    if i<10:        # i가 10보다 작으면
        continue    # 반복문 처음으로 돌아가기
    print(i, end=', ')

print()

# 1~30 사이의 수 중에서 7의 배수만 출력하기 - continue 사용
print("1~30 숫자 사이 중 7의 배수만 출력 : ")
for i in range(1, 31):
    if i%7!=0:
        continue
    print(i, end=',')