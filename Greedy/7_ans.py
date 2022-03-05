#숫자 카드 게임(p.96)

# min() 함수를 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    # print(min_value)
    result = max(result, min_value)
    # print(result)

print(result)

#2중 반복문 구조를 이용

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 #문제의 조건에서 10,000이하의 수 이므로
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)
