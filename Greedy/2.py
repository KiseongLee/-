#큰 수의 법칙(처음_2022.03.03) --> 못품
N, M, K = map(int, input().split())

n = list(map(int, input().split()))

n.sort(reverse=True)

sum = 0
for _ in range(K):
    sum += n[0]

sum += n[1]

if M - K - 1 > 0 and M - K - 1 < K:
    sum = sum + n[0]*(M-K-1)
elif M - K - 1 > K:
    sum = sum + n[0]*K
    sum = sum + n[1]

print(sum)

#큰 수의 법칙(복습_2022.03.04)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort(reverse=True)

first = data[0]
second = data[1]
result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0:
        break

    result += second
    m -= 1

print(result)
