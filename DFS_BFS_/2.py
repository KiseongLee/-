# DFS 예제
def dfs(graph, v, visited):     # DFS 메서드 정의

    visited[v] = 1              # 현재 노드를 방문 처리
    print(v, end=" ")           

    for i in graph[v]:          # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
       if not visited[i]:
           dfs(graph, i, visited) 

graph = [                       # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] 
]

visited = [False] * 9           # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

dfs(graph, 1, visited)          # 정의된 DFS 함수 호출

#BFS 예제
from collections import deque

def bfs(graph, start, visited):         # BFS 메서드 정의

    queue = deque([start])              # 큐(Queue) 구현을 위해 deque 라이브러리 사용

    visited[start] = True               # 현재 노드를 방문 처리
 
    while queue:                         # 큐가 빌 때까지 반복

          v = queue.popleft()           # 큐에서 하나의 원소를 뽑아 출력
          print(v, end=" ")

          for i in graph[v]:            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
                if not visited[i]:
                   queue.append(i)
                   visited[i] = True

graph = [                           # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]

    ]

visited = [False]*9                # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

bfs(graph, 1, visited)             # 정의된 BFS 함수 호출
