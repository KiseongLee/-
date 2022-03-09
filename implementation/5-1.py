'''
if 조건문을 하나씩 수행하도록 하고, 4번 정도 수행하면 되지 않을까 고민했지만
이렇게 되면 d =1 로 시작하고, d = 0 , 3, 2 순으로 간다. 만약에
d = 0 일때 조건이 맞아 한 칸 갈 수 있다면 값이 바뀌면서 한칸 갈 수 있다.
하지만 바로 반복문을 나와야 하는데 안그러면 한 칸 이동한 상태에서 또 반복이 진행되기 때문에 오류가 발생한다.
반복문 break를 사용하면 밑에 것이 또 진행이 되지 않고 이렇게 구현이 되지 않았다...
참고용으로 올려둔다.
'''

n, m = map(int, input().split())
a, b, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
count = 1

while True:
   
    for _ in range(4):
     if d == 0 and map[a-1][b] == 0:
        a = a-1
        b = b
        map[a][b] = 1
        count += 1
        
        if d == 1 and map[a][b-1] == 0:
        
            a = a
            b = b-1
            map[a][b] = 1
            count += 1
            
            if d == 2 and map[a+1][b] == 0:
                  a = a+1
                  b = b
                  map[a][b] = 1
                  count += 1

                  if d == 3 and map[a][b+1] == 0:
                       a = a
                       b = b+1
                       map[a][b] = 1
                       count += 1
                       break
                  else: 
                      d -= 1
                      if d == -1:
                         d = 3
         
#  if map[a-1][b] == 1 and map[a+1][b] == 1 and map[a][b+1] == 1 and map[a][b-1] == 1:
 #     break
 
 
print(count)


'''
