'''
트리의 지름 구하는 방법
1. 최상위 루트 노드 기준 으로 가장 멀리 떨어져 있는 노드 X 를 찾음
2. X 노드 기준 으로 가장 멀리 떨어져 있는 Y를 찾음
3. X-Y 거리가 트리의 가장 큰 지름이 됨
'''
import sys;
from collections import deque

sys.stdin = open('sample_input')


# 시작 노드(root = 1) 에서 가장 길이가 긴 y 찾는 함수
def PRE(v):
    if v == 0:
        return
    # print(T[v], end=' ')
    li.append(nums[v])
    PRE(L[v])
    PRE(R[v])
    sumL.append([sum(li), v])
    li.pop(-1)


# 루트와 가장 거리가 먼 노드를 기준
# 이와 가장 거리가 먼 노드 까지의 길이 = 지름
# 길이를 리스트에 다 집어넣고 max 값 찾으면 될라나

def bfs(v):
    # 일단 냅다 처음 노드를 넣음
    visted = [0] * (V + 1)
    find_DM.append([v, nums[v]])
    while find_DM:
        pass
        now_node, node_len = find_DM.popleft()
        # 아직 방문 안한 상태
        if visted[now_node] == 0:
            visted[now_node] = 1
            n = P[now_node]
        if visted[L[n]] != 1:
            find_DM.append([L[n], nums[L[n]]])
        else:
            pass
        if visted[R[n]] != 1:
            find_DM.append([R[n], nums[R[n]]])
        else:
            pass
        DM.append()
        # 일반적인 bfs 를 생각해보자
        # 방문 처리를 해줄 애를 만들어주고
        # 방문하면 1로 바꾸고

        # 여기서는?
        # 방문한 위치를 바꿔주는건 동일할듯
        # 추가적으로 저장할게 뭐가있을까 내 길이, 쟤 길이


# 리프 노드 찾기
#
# def find_leaf(v):
#     if v == 0:
#         return 0
#     l = find_leaf(L[v])
#     r = find_leaf(R[v])
#
#     # 왼쪽 오른쪽 검사해봤는데 둘 다 없으면 리프노드임
#     if l == 0 and r == 0:
#         leaf.append(v)
#
#     return leaf


V = int(input())

P = [0] * (V + 1)
L = [0] * (V + 1)
R = [0] * (V + 1)
nums = [0] * (V + 1)

find_DM = deque()
DM = deque()

li = []
sumL = []
for i in range(V - 1):
    p, c, num = map(int, input().split())

    P[c] = p

    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c

    nums[c] = num

# 최상위 루트를 기준 으로 모든 리프 노드를 찾음

# 순회 해서 가장 루트와 가장 멀리 떨어져 있는 리프 노드를 찾음

PRE(1)
max1 = max(sumL)
maxnode1 = max1[1]

print(sumL)

# bfs 를 통해서 루트랑 가장 멀리 떨어진 애 - 멀리 떨어진 애 구함
bfs(maxnode1)

print(nums)
# print(sumL)

# print(max1)
# print(maxnode1)

li = []
dimeter = []
