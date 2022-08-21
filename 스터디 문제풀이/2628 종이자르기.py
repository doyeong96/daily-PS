# 10, 8
r, c = map(int, input().split()) # r c 길이를 입력
loop = int(input()) #자르는 반복 횟수
divL = []
rc = [] # r 을 자른 만큼의 길이
cc = [] # c 를 자른 만큼의 길이
for _ in range(loop):
    div, num = map(int, input().split())
    divL.append((div, num))
# print(divL)
sortedDiv = sorted(divL, reverse=True)
# print(sorted(divL), reversed = True)
# print(sortedDiv)
'''
    num 을 기준으로 정렬해서 큰 숫자부터 먼저 오게 하면
    무조건 큰 숫자부터 자르기 때문에 음수값이 나오지 않는다. 
'''
for i in range(len(sortedDiv)):
    # print(sortedDiv[i])
    # print(sortedDiv[i][0], sortedDiv[i][1])
    # print(sortedDiv[i][1])
    if sortedDiv[i][0] == 0:
        c2 = c - sortedDiv[i][1]
        cc.append(c2)
        c = c - c2
    else:
        r2 = r - sortedDiv[i][1]
        rc.append(r2)
        r = r - r2
else:
    cc.append(c)
    rc.append(r)

print(max(rc) * max(cc))


#     if div == 0: # 세로길이를 자름
#         c2 = c - num
#         cc.append(c2)
#         c = c - c2
#     else: # 가로 길이를 자름
#         r2 = r - num
#         rc.append(r2)
#         r = r - r2
# else:
#     cc.append(c)
#     rc.append(r)
#
# dap = max(rc) * max(cc)
# print(rc)
# print(cc)
# print(dap)
