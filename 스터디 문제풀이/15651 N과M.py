'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''

import sys;
sys.stdin = open('sample_input')

def BT():
    if len(dap) == M:
        print(*dap)
        return
    else:
        for num in nums:
            dap.append(num)
            BT()
            dap.pop()

N, M = map(int, input().split())
nums = [1+i for i in range(N)]
dap = []
idx = 0
BT()