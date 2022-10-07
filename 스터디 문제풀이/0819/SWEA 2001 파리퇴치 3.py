# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 우상 우하 좌하 좌상
cr = [-1, 1, 1, -1]
cc = [1, 1, -1, -1]

for test in range(int(input())):
    n, m = map(int, input().split())  # n = 파리, m = 스프레이 세기
    pari = [list(map(int, input().split())) for _ in range(n)]
    maxH = 0

    for sr in range(n):
        for sc in range(n):
            hap1 = pari[sr][sc]
            hap2 = pari[sr][sc]
            for i in range(4):
                for j in range(1, m):
                    nr = sr + dr[i] * j
                    nc = sc + dc[i] * j
                    ncr = sr + cr[i] * j
                    ncc = sc + cc[i] * j

                    if 0 <= nr < n and 0 <= nc < n:
                        hap1 += pari[nr][nc]

                    if 0 <= ncr < n and 0 <= ncc < n:
                        hap2 += pari[ncr][ncc]
            if maxH < hap1:
                maxH = hap1
            if maxH < hap2:
                maxH = hap2

    print(f'#{test + 1} {maxH}')