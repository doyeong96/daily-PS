'''
l = 육지
w = 바다

보물 상자의 위치를 내가 어떻게 알아

상하좌우로 이웃한 육지로만 이동 가능


가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀 있다.
cnt 값 때려 넣어서 맥스인 위치

찾고자 하는건
두 곳 사이를 최단 거리로 이동할때의 시간
'''
import sys;
sys.stdin = open('sample_input')
from collections import deque

# 걍 아무 거나 때려 넣음
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(i, j):
    bomul = 0
    visted = [[0] * c for _ in range(r)]
    q = deque()
    visted[i][j] = 1
    q.append((i, j))
    while q:
        sr1, sc1 = q.popleft()
        for d in range(4):
            nr = sr1 + dr[d]
            nc = sc1 + dc[d]
            # 범위체크 해주고, 움직이는 위치가 땅일때만 가고, 아직 방문 안했고
            if 0 <= nr < r and 0 <= nc < c and zido[nr][nc] == 'L' and visted[nr][nc] == 0:
                visted[nr][nc] = visted[sr1][sc1] + 1
                # if bomul < visted[nr][nc]:
                #     bomul = visted[nr][nc]
                bomul = max(bomul, visted[nr][nc])

                #bomul = []
                #bomul.append(cnt, nr, nc)

                # 원래는 이런식 으로 해서 가장 거리가 먼 육지의 위치를 찾아서

                # bomul = max(max(visted)) 시간초과의 주범인듯?
                q.append((nr, nc))
    return bomul - 1

cnt = 0
r, c = map(int, input().split())
zido = [input() for _ in range(r)]
for sr in range(r):
    for sc in range(c):
        # 육지일때만 거리찾으러 가야됨
        if zido[sr][sc] == 'L':
            find = bfs(sr, sc)
            if cnt <= find:
                cnt = find
print(cnt)