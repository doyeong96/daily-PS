import sys;
sys.stdin = open('sample_input')
'''
1 BT 함수
    1-1 요구한 조건을 만족했을 때 함수 호출부로 되돌아가는 부분
    1-2 요구 조건을 만족하지 못했을 때 조건을 만족하게 만드는 부분
2 입력처리
'''
def BT():
    global makenum
    # 만든 조합의 길이 m 일때
    if M == len(makenum):
        print(*makenum)
        return
    # 만든 조합의 길이가 m 이 아닐때
    else:                               # makenum = [ ]
        for num in nums:                # nums를 하나하나 쪼갠다 ex [1,2,3,4] => 1, 2, 3, 4
            if num in makenum:          # 리스트에 있는 숫자랑 현재 num 이랑 같으면 무시
                continue
            else:
                makenum.append(num)     # 현재 숫자를 리스트에 넣어줌
                BT()                    # 재귀 호출
                makenum.pop()

'''
만약 num 이 1일때 BT를 호출하면
makenum 에는 1이 들어가있고
다시 num이 1일때부터 for 문을 돈다
num이 1~4까지 다시 돌고
전부 끝나면 다시 
num 이 1인 상태일때의 BT함수 위치로 오고 pop 해준 뒤 다시 for문을 돌게된다.
'''

N, M = map(int, input().split())
nums = [1 + i for i in range(N)]
makenum = []
# dap = []
# # idx = 0
BT()