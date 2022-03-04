#ans1
N, M, K = map(int, input().split())

n = list(map(int, input().split()))

n.sort(reverse=True)

first = n[0]
second = n[1]
sum = 0

while True:
    for i in range(K):
        if M == 0:
            break
        sum += first
        M -= 1
    
    if M == 0:
        break

    sum += second
    M -= 1
 
print(sum) 

#ans2
N, M, K = map(int, input().split())

n = list(map(int, input().split()))

n.sort(reverse=True)

first = n[0]
second = n[1]

count = ((M // (K+1))*K) + M%(K+1)

sum = count * first + (M-count) * second

print(sum) 
