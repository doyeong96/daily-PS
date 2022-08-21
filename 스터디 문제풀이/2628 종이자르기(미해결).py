# 10, 8
r, c = map(int, input().split()) # r c 길이를 입력
loop = int(input()) #자르는 반복 횟수
rc = [] # r 을 자른 만큼의 길이
cc = [] # c 를 자른 만큼의 길이
for _ in range(loop):
    div, num = map(int, input().split())

    if div == 0: # 세로길이를 자름
        c2 = c - num
        cc.append(c2)
        c = c - c2
    else: # 가로 길이를 자름
        r2 = r - num
        rc.append(r2)
        r = r - r2
else:
    cc.append(c)
    rc.append(r)

dap = max(rc) * max(cc)
print(rc)
print(cc)
print(dap)
