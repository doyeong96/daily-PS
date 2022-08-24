'''
    입력
    1줄 :        면적 1당 자라는 참외의 갯수
    2줄 이하 ~ : 방향, 길이

    동, 서 방향 = 세로
    남, 북 방향 = 가로

    예제기준)
    가로 가장 긴 길이 * 세로 가장 긴 길이 = 전체 면적
    가로 가장 짧은 길이 * 세로 가장 짧은 길이 = 잘린 면적
    전체 면적 - 잘린 면적 = 참외밭의 면적

    접근
    입력을 받을때 방향 을 기준으로 각각 리스트에 넣어준다
    if d == 1, or d == 2:
    세로 리스트
    d == 3, d== 4
    가로 리스트
    리스트의 가장 큰 값을 뽑아서 전체 면적을 구하고
    리스트의 가장 작은 값을 뽑아서 잘린 면적을 구한다.
    두 면적을 빼서 면적당 참외의 개수를 곱해준다.


    가로 리스트의 가장 긴 변의 인덱스 위치와
    세로 리스트의 동일한 인덱스 위치, +1 번째 인덱스 위치의 세로길이 = 가장 긴 가로의 양 옆의 길이
    양 옆의 길이를 빼주면 작은 사각형의 세로길이

    가로의 가장 긴 길이 - 가로리스트 마지막 길이 = 작은 사각형의 가로길이

7
4 50
2 160
3 30
1 60
3 20
1 100




160 60 100
50 30 20

1
1 1
4 10
2 10
3 1
1 9
3 9
'''

fruit = int(input()) #면적당 참외
allL = []
cL = [] # 세로 리스트
rL = [] # 가로 리스트
for _ in range(6): # 6각형 이라 6번
    d, meter = map(int, input().split())
    allL.append(meter)
    if d == 1 or d == 2:
        cL.append(meter)
    else:
        rL.append(meter)

# 큰 사각형 넓이
allS = max(cL) * max(rL)

#작은 사각형의 세로
mcIdx = allL.index(max(cL))

if mcIdx + 1 <= len(allL):
    cutR = max(cL) - allL[mcIdx-1]
elif 0 >= mcIdx-1:
    cutR = max(cL) - allL[mcIdx + 1]
else:
    nearR1 = (allL[mcIdx-1])
    nearR2 = (allL[mcIdx+1])
    if nearR1 < nearR2:
        cutR = nearR2 - nearR1
    else:
        cutR = nearR1 - nearR2
# cutR 작은사각형의 세로

#작은 사각형의 가로
mrIdx = allL.index(max(rL))

if mrIdx+1 <= len(allL):
    cutC = max(cL) - allL[mrIdx-1]
elif 0 >= mrIdx-1:
    cutC = max(cL) - allL[mrIdx+1]
else:
    nearC1 = (allL[mrIdx - 1])
    nearC2 = (allL[mrIdx + 1])
    if nearC1 < nearC2:
        cutC = nearC2 - nearC1
    else:
        cutC = nearC1 - nearC2

# cutC 작은 사각형의 가로

cutS = cutR * cutC

bap = allS - cutS

print(bap*fruit)





# print(cL)
# print(rL)
# print(allS)
# print(cL.index(max(cL)))
# print(cutR)
# print(cutC)

# print(cutS)
# print(bap)




# cut = min(cL)*min(rL)
# print(all, cut)
# bap = all-cut
# print(bap)
# dap = bap * fruit
# print(dap)