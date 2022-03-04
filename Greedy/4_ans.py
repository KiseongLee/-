
 #가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?
 #N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있습니다.
 # 다시 말해 K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있습니다.
 # 또한, N은 항상 1에 도달하게 됩니다.

n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)

# log 시간 복잡도를 가지므로 N의 값이 커질수록 더 연산양이 적어져서 유리하다.
