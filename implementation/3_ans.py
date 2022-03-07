
'''
요구사항대로 충실히 구현하면 되는 문제입니다.
나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인한다.
 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의한다.
'''

#현재 나이트의 위치 입력 받기 

input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord("a") + 1

steps = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)] #말의 이동 가능 범위를 한 list로 받음

result = 0 #count값
for step in steps: # 말의 이동 가능 범위를 list의 원소 값으로 반복문 실행
    next_row = row + step[1] # 각 원소의 index 1 값이 행의 값
    next_column = column + step[0] # 각 원소의 index 0 값이 열의 값

    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8: #예외 값 처리를 위한 조건문 실행
        result += 1 # count값 1씩 추가

print(result) #출력
