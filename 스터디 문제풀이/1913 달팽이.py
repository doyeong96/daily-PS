# n = int(input())
# num = int(input())
#
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# # 하 우 상 좌
# # arr[0][0] 위치부터 시작할 것이기 때문에
# # 방향은 하 우 상 좌 순
# dalpang = [[0]*n for _ in range(n)] # 2차원 배열 생성
# r = c = 0
# cnt = n*n
# # 첫번째 값이 배열을 곱한 가장 큰 값이기 때문에
# dalpang[r][c] = cnt
# # 0,0에 최대값을 넣어줌
#
# d = 0 # 방향제한
# cnt -= 1
#
# while dalpang[n//2][n//2] != 1: # 1이 들어가야 하는 위치가 1이 아닐때까지
#     # 1이 들어가있는 자리는 n을 2로나눈 몫의 위치이기 때문에
#     nr = r + dr[d]
#     nc = c + dc[d]
#
#     if 0 <= nr < n and 0 <= nc < n and dalpang[nr][nc] == 0: #범위 제한
#         r = nr
#         c = nc
#         dalpang[r][c] = cnt
#         cnt -= 1
#     else: # 방향 전환
#         d = (d + 1) % 4
#
# # for lst in dalpang: # 달팽이 배열 프린트
# #     print(*lst)
#
# for i in dalpang:
#     for j in i:
#         print(j, end=' ')
#     print()
#
# for i in range(n):
#     for j in range(n):
#         if dalpang[i][j] == num:
#             print(i+1, j+1)

'''
9 2 3
8 1 4
7 6 5

'''
n = int(input())
#숫자 입력
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
#하 우 상 좌

#달팽이
arr = [[0] * n for _ in range(n)]
#초기화
r = c = 0
d = 0
cnt = n*n
arr[r][c] = cnt
cnt -= 1
#반복
while arr[n//2][n//2] != 1:
    nr = r + dr[d]
    nc = c + dc[d]
    # 범위 제한
    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
        # 방향 이동
        r = nr
        c = nc
        arr[r][c] = cnt
        cnt -= 1
    else:
        d = (d+1) % 4
for arr in arr:
    print(*arr)