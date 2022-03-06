#4-2(p.113)
#2번째 푼 것(2022.03.06)

n = int(input()) # N시 59분 59초까지이므로 N을 입력

count = 0 # count 정의
'''
구현
1. 시간의 값을 받아서 입력을 받아올 수 있어야 한다. 
--> 삼중 반복문을 통해 구현
2. 3이 포함된 모든 경우의 수를 구한다.
--> 숫자를 문자열화 한 후, 조건문을 부여하여 값을 구해주면된다 // 이것을 구현못해서 정답을 봄.
'''
for i in range(n+1):
    for j in range(60):
        for k in range(60):
           a =  str(i) + str(j) + str(k)
           if "3" in a:
               count += 1
print(count) #출력
