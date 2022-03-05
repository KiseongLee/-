#5 곱하기 혹은 더하기

#1(2022.03.04)

n = input()

result = int(n[0])


for i in range(1, len(n)):
    
    if int(n[i]) == 0 or int(n[i]) == 1 or result == 0 or result == 1:
        result += int(n[i])
    
    else:
        result *= int(n[i])

print(result)
 
#2(2022.03.05)

n = list(map(int, input()))

'''result = 0

if n[0] <= 1 or n[1] <= 1:
    result = n[0]+n[1]
else:
    result = n[0]*n[1]

for i in range(2, len(n)):

    if result <= 1 or n[i] <= 1:
        result += n[i]
    else:
        result *= n[i]

print(result)''' --> 수정 전


result = n[0]

for i in range(1, len(n)):

    if result <= 1 or n[i] <= 1:
        result += n[i]
    else:
        result *= n[i]

print(result)  --> 수정 후
