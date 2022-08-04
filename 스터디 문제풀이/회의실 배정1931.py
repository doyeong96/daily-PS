'''
    입력 
    1 회의 수
    2 회의의 시작시간 끝시간
'''
'''
    회의실은 한개밖에 없다
    0번 인덱스의 회의는 무조껀 들어가게 됨 -> 빈 리스트 만들어서 추가
    회의 끝나는 시간보다 시작 시간이 작으면 i[1]<i[0] 사용 불가능
    사용 가능한 회의를 만나면 리스트에 추가 
    -> 리스트[-1]으로 가장 최근에 들어간 회의를 기준으로 검토
    전부 다 추가하면 리스트의 길이를 출력
'''

n = int(input())
meet = []
for i in range(n):
    meeting = list(map(int,input().split()))
    meet.append(meeting)

use = [meet[0]]

for i in range(1,len(meet)):
    # print(use[-1][1])
    # print(meet[i][0])
    if use[-1][1] <= meet[i][0]: 
        use.append(meet[i])
print(use)
print(len(use))

# print(meet)
# print(use[-1][1])

# print(meet[0][1])  meet[i][0] 이랑 use[-1][1] 을 비교할 수 있으면 될텐데
# print(use[1])