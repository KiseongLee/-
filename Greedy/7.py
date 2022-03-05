#숫자 카드 게임(p.96)(2022.03.05. 11:00)


'''
#2차원 배열 받기
1.
mylist = [0 for _ in range(3)]

print(mylist)

for i in range(3):
    mylist[i] = list(map(int, input().split()))

print(mylist)
'''

'''
2.
mylist = []
for i in range(3):
    mylist.append(list(map(int, input().split())))

print(mylist)
'''

'''
3.
mylist = [list(map(int, input().split())) for _ in range(3)]

print(mylist)
'''

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    data[i].sort()

# print(data)  / 확인용

max = data[0][0]

for j in range(1, n):
    if data[j][0] >= max:
        max = data[j][0]

print(max)
