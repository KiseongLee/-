
#모험가 길드
#1(2022.03.04)
n = int(input())

data = list(map(int, input().split()))

data.sort()

count = 0
result = 0

for i in range(len(data)-count):
    count = 0
    while data[i] > count:
        count += 1

    result += 1
    

print(result)

--> 풀지 못함

#2(2022.03.05)
n = int(input())
data = list(map(int, input().split()))

data.sort()
count = 0
for i in data:
    if n >= i:
       count += 1
       n -= i
    else: break

print(count)

--> 풀지 못함/idea 생각이 중요 
