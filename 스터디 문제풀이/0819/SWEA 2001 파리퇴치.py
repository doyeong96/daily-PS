for test in range(int(input())):
    n, m = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(n)]
    mhap = 0
    for sr in range(n - m + 1):
        for sc in range(n - m + 1):
            hap = 0
            for r in range(sr, sr + m):
                for c in range(sc, sc + m):
                    hap += pari[r][c]
            if mhap < hap:
                mhap = hap
    print(f'#{test + 1} {mhap}')
