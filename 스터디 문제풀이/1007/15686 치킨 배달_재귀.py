def dfs(check, dep):
    # 선택한 치킨집 방문 처리
    global dvisit, dap, road

    if len(check) == m: # and len(check) != 0:
        hap = 0
        minV = 987654321
        # 집 기준 으로 거리 측정
        for hr, hc in house:
            for cr, cc in check:
                hap = abs(hr - cr) + abs(hc - cc)
                if minV > hap:
                    minV = hap

            road += minV
            minV = 987654321
            hap = 0
        if dap > road:
            dap = road
        road = 0
        return

    for i in range(dep, len(chicken)):
        dfs(check + [chicken[i]], i+1)

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
# house = [[0]*n for _ in range(n)]
chicken = []
house = []
road = 0
for i in range(n):
    for j in range(n):
        # 가정집
        if MAP[i][j] == 1:
            house.append((i, j))
            # house[i][j] = 1
        if MAP[i][j] == 2:
            chicken.append((i, j))

dvisit = [0] * len(chicken)
dap = 987654321
dfs([], 0)
print(dap)