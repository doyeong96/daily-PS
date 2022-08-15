'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
n, m = map(int,(input().split()))               #맵 크기
r, c, direction = map(int,(input().split()))    #현 위치 r, 현 위치 c, 바라보는 방향
zido = [list(map(int, input().split())) for _ in range(n)]
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
zido[r][c] = '*'
cnt = 0
while True:
    # 1. 시작하자 마자 회전해야 하기 때문에
    # 2. 진행이 불가능하면 회전해야 하기 때문에
    direction -= 1
    if direction == -1:
        direction = 3

    nr = r + dr[direction]
    nc = c + dc[direction]

    if zido[nr][nc] == 0: # 회전해서 바라보는 앞이 0 이면
        zido[nr][nc] ='*' # 그 자리를 * 으로 채우고
        r = nr
        c = nc
        cnt = 0

    if zido[nr][nc] != 0: # 회전해서 바라보는 방향이 0이 아니면
        cnt += 1 # 카운트를 증가시키고
        if cnt == 4: #만약 카운트가 4가 되면
            direction -= 1
            if zido[nr][nc] == 1:
                break
            elif zido[nr][nc] == 0:
                zido[nr][nc] = '*'
                cnt = 0


visit = 0
for i in range(n):
    for j in range(m):
        if zido[i][j] == '*':
            visit += 1
print(visit)