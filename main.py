from collections import deque

n, m, v = map(int, input().split(' '))
graph = [[] for _ in range(n+m + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
  n1, n2 = map(int, input().split(' '))
  graph[n1].append(n2)
  graph[n2].append(n1)

#graph를 낮은 순서대로 sort
for g in graph:
  g.sort()


def DFS(v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      DFS(i, visited)


DFS(v, visited)


def BFS(v, visited):
  queue = deque([v])
  visited[v] = True
  print(v, end=' ')
  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        print(i, end=' ')


visited = [False for _ in range(n + 1)]
print("\n", end='')
BFS(v, visited)
