def dfs(month, pay):
    global now_pay
    # 12개월 다 체크
    if month >= 12:
        if now_pay >= pay:
            now_pay = pay
        return

    # 수영장 이용료가 최소 이용료(현재 가장 적게 낼 수 있는 이용료)를 넘었을때
    if now_pay < pay:
        return

    # if month < 12:
    # 1일권을 이용할때
    dfs(month + 1, pay + (plan[month] * fee[0]))

    # 한달권을 이용할때
    dfs(month + 1, pay + fee[1])

    # 3개월권을 이용할때
    dfs(month + 3, pay + fee[2])


for test in range(int(input())):
    # 0 = 1일권, 1 = 한달권, 2 = 3개월권 3 = 1년권
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    # 1년권 비용은 일단 넣고 시작
    now_pay = fee[3]
    # 1월부터 체크 (인덱스는 0)
    if sum(plan) < 365:
        dfs(0, 0)
    print(f'#{test+1} {now_pay}')