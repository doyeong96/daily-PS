'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''
'''
n,m 1과 유사한 유형이지만
같은 숫자를 여러번 골라도 무관하기 때문에 
현재 dap 에 넣으려는 숫자가 이미 들어가있을때 
무시하고 다음단계로 넘어가는 조건을 빼줬다.
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