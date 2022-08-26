import sys; sys.stdin = open('농작물 수확.txt')
# for test in range(int(input())):
#     n = int(input())
#     bap  = [list(map(int, input())) for _ in range(n)]
    # garo = 0
    #
    # # 좌 우
    # dr = [0, 0]
    # dc = [-1, 1]
    #
    # start = end = n//2
    #
    # for d in range(2):
    #     for k in range(1, n):
    #         nr = start + dr[d] * k
    #         nc = end + dc[d] * k
    #         if 0 <= nr < n and 0 <= nc < n:
    #             garo += bap[nr][nc]
    # print(garo)
    # #st = 2 end+1 = 3
    # up = 0
    # for ur in range(n//2):
    #     for uc in range(start, end + ur + 1):
    #         up += bap[ur][uc]
    #
    #         if ur < start:
    #             start -= 1
    #
    # down = 0
    # for downR in range(n//2 + start, n + start):
    #     for downC in range(n//2 - start, n - start):
    #         down += bap[downR][downC]
    #
    #         if downR > n//2:
    #             start += 1

def UPR():
    global hap
    for i in range(start, mid+1): #가장 위쪽 중앙부터 아래로 한칸씩 증가하면서 삼각형을 이룸
        for j in range(mid - i, n - mid + i):
            hap += filed[i][j]
    return hap

def DNR():
    global hap
    global start
    for r in range(end, mid, -1): # -1씩 감소하면서 중앙선 바로 아래까지 하락
        for c in range(mid - start, mid + 1 + start):
            # 아래로 한칸 내려갈때마다 왼쪽은 1씩 감소 오른쪽은 1씩 증가 필요
            hap += filed[r][c]
        start += 1 # for c 가 끝나면 시작점을 1씩 증가시킨다
    return hap
for test in range(int(input())):
    n = int(input())
    filed  = [list(map(int, input())) for _ in range(n)]
    start = 0
    mid = n//2
    end = n -1
    hap = 0
    UPR()
    DNR()
    print(f'#{test + 1} {hap}')







