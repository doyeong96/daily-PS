# now = input() #처음 위치
# hang = int(now[0])
# 행
# yeol = int(now[1])
# 열(알파벳으로 입력받는 법을 모르겠어서 일단 숫자로)
#
# move = [(-1, 2), (1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
#
# for i in move:
#
'''
    now = input() => 처음 위치
    hang = int(now[0]) => 행 - y
    yeol = int(now[1]) => 열 - x
    움직임 (x,y)
    -1,2 / 1,2 / 1,-2 / -1,-2 / -2,1 / -2,-1 / 2,1 / 2,-1

'''

now = input()

dx = [-1, 1, 1, -1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

cnt = 0
for i in range(8):
    hang = int(now[1])
    yeol = int(now[0])

    hang += dx[i]
    yeol += dy[i]

    if 1 <= hang <= 8 and 1 <= yeol <= 8:
        cnt += 1
print(cnt)

