# 방향성이 필요할듯
# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


# 종료할 수 있는 조건 = 시작 위치와 현재 위치가 동일할때 종료 하고 최대값을 비교함
# 하지만 움직인 카운트가 없으면 한군데만 간거니까 안됨

# 되돌아가야 하는 조건 = 벽을 만난 경우, 이미 먹은 디저트(숫자) 를 또 만난 경우

# 그냥 일단 이동은 하되 이동 하고 나서 체크 하는게 편할듯
def DFS(x, y, breads, d):
    global maxV

    # 아직 못먹은 디저트면 먹으러가고
    # if val not in breads:
    #     breads.append(val)
    # else:
    #     return
    # 먹어본 디저트면 방향을 바꿔서 다른 위치로 이동해야 하기 때문

    # 디저트 투어를 옳바르게 마친 경우
    # 현재 위치 = 출발 위치, 방향 3번 바꿈, 디저트 하나 이상 먹음
    if d == 3 and sr == x and sc == y and len(breads) > 2:
        # 옳바르게 투어를 마쳤으면 몇개의 디저트를 먹었는지 갱신
        if maxV < len(breads):
            maxV = len(breads)

    # 투어를 하러 이동 하는 경우
    # 범위 안에 있어야 하고, 현재 먹으려는 디저트를 아직 먹지 않은 경우
    if 0 <= x < n and 0 <= y < n and arr[x][y] not in breads:
        # 직진 하는 경우
        new_bread = breads + [arr[x][y]]
        nr = x + dr[d]
        nc = y + dc[d]
        DFS(nr, nc, new_bread, d)
        # 꺾어야 하는 경우
        # 3 넘어 가면 델타 범위 벗어남
        if d < 3:
            nr = x + dr[d+1]
            nc = y + dc[d+1]
            DFS(nr, nc, new_bread, d+1)

for test in range(int(input())):
    breads = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = -1
    for r in range(n):
        for c in range(n):
            sr, sc = r, c
            # 현재 좌표1, 2(변경 시켜줄 좌표), 디저트 종류, 델타 사용을 위함, 시작 좌표 1, 2
            DFS(r, c, [], 0)
            breads = []
    print(f'#{test+1} {maxV}')

