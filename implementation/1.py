
#4-1(p.110)

#1(2022.03.04)
n = int(input())  # N*N의 정각형 공간 입력
data = list(input().split()) #계획서 내용 입력(상하좌우)


x, y = 1, 1  #현재 위치

for i in data: 

    if i == 'L' and y>1 :
        x = x
        y = y - 1
    
    if i == 'R' and y < n: 
        x = x
        y = y + 1
    
    if i == 'U' and x>1 :
        x = x -1
        y = y
    
    if i == 'D' and x > n:
        x = x + 1
        y = y
''' 반복문 수행, 2가지를 해결해야함
1. R L U D로 출력하므로 각각 입력할 때, 좌표를 더해줌 예를 들면, L --> (0, -1) 
2. 공간의 크기를 벗어났을 때는 무시 ex) (1,4) --> U입력(-1,0) --> (0,4)가 되어야하는데 공간이 벗어나므로 무시 --> (1,4)
   각 입력 시, 벗어나지 않는 조건을 추가해줌(L, y>1)
'''   
print(x, y) #출력

#2(2022.03.06)
n = int(input())

data = input().split()

x,y = 1, 1


for i in range(len(data)):

   if data[i] == "R":
          nx = x
          ny = y + 1
   elif data[i] == "L":
           nx = x
           ny = y - 1
   elif data[i] == "U":
            nx = x - 1
            ny = y
   elif data[i] == "D":
            nx = x +1
            ny = y

 # 2가지 해결해야될 것 중, 1번은 비슷하게 넣어줌
 
   if  nx < 1 or nx > n or ny < 1 or ny >n:
        continue
# 2번은 아래와 같이 한꺼번에 처리해줄 수 있게 continue를 씀
   x = nx
   y = ny
  
print(x, y)
