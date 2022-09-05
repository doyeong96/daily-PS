import sys;

sys.stdin = open('sample_input')


def BT(idx):
    if len(dap) == M:
        print(*dap)
        return
    else:
        while idx != N:
            num = nums[idx]
            dap.append(num)
            BT(idx)                 # idx를 그냥 넘겨 주는 이유는 같은 값을 가지는 중복이 허용 되기 때문
            idx += 1                # 함수를 계속 호출하다 while문이 끝나면 호출 대기상태를 돌아서 idx 기준값이 0일때로 돌아오고 그때 idx를 증가시켜 주기 때문에
                                    # 그 이후로는 idx를 1부터 시작할 수 있음
            dap.pop()
        pass


N, M = map(int, input().split())
nums = [1 + i for i in range(N)]
idx = 0
dap = []
BT(idx)
