#5-1 스택 예제
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제-삽입(1)-삽입(4)-삭제()
'''
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
'''
# 5-2 큐 예제
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
'''
from collections import deque

queue = deque() # 큐(Queue) 구현을 위해 deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
'''
# 5-3 재귀 함수 예제
'''
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()  # RecursionError: maximum recursion depth exceeded while calling a Python object
                      # 오류 메시지 : 재귀의 최대 깊이를 초과했다는 내용. 보통 파이썬 인터프리터는 호출 횟수 제한이 있다. 이 한계를 벗어남.
                      # 따라서 무한대로 재귀 호출을 진행할 수는 없다.
'''

# 5-4 재귀 함수 종료 예쩨
'''
def recursive_function(i):

    if i == 100:
        return   # 100번째 출력했을 때 종료되도록 종료 조건 명시
    
    print(i,"번째 재귀 함수를 호출합니다.", i+1,"번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀 함수를 종료합니다.")

recursive_function(1)
'''

# 5-5 2가지 방식으로 구현한 팩토리얼 예제
'''
def factorial_iteration(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    

print(factorial_iteration(5))
'''
'''
def factorial_recursive(n):

    
    if n <= 1:
       return 1

    return n * factorial_recursive(n-1)

print(factorial_recursive(5))
'''
