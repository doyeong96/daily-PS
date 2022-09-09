'''
    l = 암호의 길이
    c = 문자의 갯수

    조건
    최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로
    조건 만족을 위해 리스트에 들어갈때 모음인지 자음인지를 체크해준다.
    문자열은 정렬돼 있음

코드짜서 체크하는 순서

중복 안되게 모든 조합을 만든다.
'''
import sys;

sys.stdin = open('sample_input')


def BT(idx):
    global V, C
    # 조건을 만족했을 때 프린트해주게끔
    if len(dap) == l and V >= 1 and C >= 2:
        str(dap)
        print(''.join(dap))
        # dap.pop()
        return
        # 조건을 만족시킬 수 있게끔
    else:
        while idx != c:
            char = chars[idx]
            dap.append(char)
            if char in VS:
                V += 1
            else:
                C += 1
            BT(idx + 1)
            idx += 1
            a = dap.pop()
            if a in VS:
                V -= 1
            else:
                C -= 1

            # if visted[idx] == 0:
            #     char = chars[idx]
            #     dap.append(char)
            #     if char in VS:
            #         V += 1
            #     else:
            #         C += 1
            #     visted[idx] = -1
            #     BT(idx+1)
            #     visted[idx] = 0
            #     a = dap.pop()
            #     if a in VS:
            #         V -= 1
            #     else:
            #         C -= 1
            #     idx += 1

        # for i in range(c):
        #     if visted[i] == 0:
        #         dap.append(chars[i])
        #         visted[i] = -1
        #         BT()
        #         visted[i] = 0
        #         dap.pop()

        # while idx != l:
        #     char = chars[idx]
        #     dap.append(char)
        #     if char in VS:
        #         V += 1
        #     else:
        #         C += 1
        #     BT(idx + 1)
        #     idx += 1
        #     V = C = 0
        #     dap.pop()


l, c = map(int, input().split())
chars = sorted(list(map(str, input().split())))
# 모음들
VS = ['a', 'e', 'i', 'o', 'u']
visted = [0] * c
# 모음 자음 갯수
V = C = 0
dap = []
# idx = 0
BT(0)
# BT()
