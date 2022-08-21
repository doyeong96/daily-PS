'''
100 * 100 배열을 전부 0으로 채운다
입력받은 좌표에 따라 사각형을 만들고
겹치든 말든 1으로 채운다

배열을 전부 순회하면서 1을 찾으면 cnt 를 증가시킨다(시간 초과 날수도 있을듯)
cnt 를 출력한다.

좌표 입력은 4번 들어온다
r1 c1 r2 c2
범위는 r1 ~ r2 / c1 ~ c2
'''
n = 100
arr = [[0] * n for _ in range(n)]
# for
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())

    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = 1
#
# for arr in arr:
#     print(*arr)
cnt = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            cnt += 1
print(cnt)