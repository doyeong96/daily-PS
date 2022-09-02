'''
dfs 활용

1줄 - 컴퓨터 갯수 - V
2줄 직접 연결된 컴퓨터 - E
3줄 연결된 컴퓨터 쌍 V_n E_n

dfs 작성 순서
정점(V) 와 간선(E) 를 입력 받음
그래프 생성 = [[] for _ in range(v+1) 보통 1번부터 시작 하기 때문에 v+1 까지

정점과 간선으로 연결된 그래프를 입력 받음(혹은 만듬 보통 for 문으로 순회함)

유향 그래프의 경우 => 그래프[정점].append(간선)
무향 그래프의 경우 => 그래프[정점].append(간선)  그래프[간선].append(정점)

방문 배열을 생성함 visted = [0] * V+1

dfs 함수를 정의함

def DFS(v)
visited[v] = 1

for w in 그래프(v)
ii visited[w] == 0:
DFS(w) <- 재귀
필요한 요소를 return
'''
def DFS(v):
    visted[v] = 1

    for w in graph[v]:
        if visted[w] == 0:
            DFS(w)
    return visted

V = int(input())
E = int(input())
start = 1
graph = [[] for _ in range(V+1)]

for _ in range(E):
    V_n, E_n = map(int, input().split())
    graph[V_n].append(E_n)
    graph[E_n].append(V_n)

    visted = [0] * (V + 1)

# print(DFS(start))

print(sum(DFS(start))-1)









#dfs 함수 구현
def dfs(v):
    visted[v] = 1 #방문 위치에 1을 할당

    for w in graph[v]: #그래프를 하나씩 검사
        if visted[w] == 0: #방문하지 않았다면
            dfs(w) #재귀호출
    #그래프, 방문배열 호출 선택
    return visted

V = int(input()) #정점
E = int(input()) #간선

#그래프
graph = [[] for _ in range(V+1)]
#방문 배열
visted = [0] * (V + 1)
#간선 갯수만큼 트리를 입력받고 그래프에 할당
for _ in range(E):
    vn, en = map(int, input().split())
    #무향그래프
    graph[vn].append(en)
    graph[en].append(vn)

#문제에서는 1번 컴퓨터가 바이러스에 걸림
print((dfs(1)))