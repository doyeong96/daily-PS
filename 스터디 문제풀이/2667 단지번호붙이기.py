'''
1을 만나면 bfs 함수가 돌아가게끔?

bfs 함수로 큐에 1일때의 좌표를 넣고
pop 해서 쓰고

'''

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
def BFS(r, c, n): # 가로, 세로, 길이

    visited = [[0] * n for _ in range(n)]
    Q = [(r, c)]
    # 어차피 단지가 시작하는걸 발견하고 BFS 함수에 들어왔기 때문에
    # 바로 방문한 지점을 체크해주고 지워줌
    visited[r][c] = 1
    arr[r][c] = 0

    # cnt = 0
    cnt = 1
    # 왜 cnt가 -1씩 빠지는지 모르겠네

    while Q: #큐에 머가 있으면
        r, c = Q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1 and visited[nr][nc] != 1: #범위체크, 배열이 단지일때, 방문하지 않은 곳일때
                arr[nr][nc] = 0 # 0 으로 안바꿔주니까 계속 들어가서 1 갯수만큼 cnt가 들어갔던거네
                cnt += 1
                Q.append((nr, nc))
                visited[nr][nc] = 1
    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
danzi =[] # 몇개 단지인지 len 으로 할거임

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            danzi.append(BFS(r, c, n))
# danzi = sorted(list(set(danzi)))
print(len(danzi))
danzi.sort()
for i in range(len(danzi)):
    print(danzi[i])
