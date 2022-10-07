for test in range(int(input())):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    m = n//2
    dap = 0

    for r in range(n):
        if r <= m:
            for c in range(m - r, m + r + 1):
                dap += arr[r][c]
        else:
            for c in range(r - m, n - (r - m)):
                dap += arr[r][c]

    print(f'#{test + 1} {dap}')