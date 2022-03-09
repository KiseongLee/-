# 게임개발(p.118)(03.07)

'''
d값과 상하좌우의 값을 기준으로 4번씩 반복해서 코드를 구현했다.
하지만, 상 하 좌 우 따로 따로 조건문을 입력하다보니 순서에 문제가 생겼고, 
또한, 상하좌우 값이 1이면 한 칸 뒤로 가야하는 것도 구현하지 못함.

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
        break
    else: 
         d = 3  # continue 이것을 잘 못하겠더라..ㅠㅠ
        

    if d == 1 and map[a][b-1] == 0:
        
        a = a
        b = b-1
        map[a][b] = 1
        count += 1
        break

    else:
        d = 0
        
    
    if d == 2 and map[a+1][b] == 0:
        a = a+1
        b = b
        map[a][b] = 1
        count += 1
        break
    else:
        d = 1
        

    if d == 3 and map[a][b+1] == 0:
        a = a
        b = b+1
        map[a][b] = 1
        count += 1
        break
    else: 
         d = 2

 if map[a-1][b] == 1 and map[a+1][b] == 1 and map[a][b+1] == 1 and map[a][b-1] == 1:
    break

print(count)
