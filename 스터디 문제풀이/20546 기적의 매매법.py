money = int(input())
juga = list(map(int, input().split()))
junMoney = sungMoney = money
junStcok = sungStock = 0

'''
준성이는 가진돈이 주가보다 크면
죄다 주식을 산다
junStcok += junMoney // juga[i] 로 주식 보유량을 늘려주고
junMoney = junMoney % juga[i] 로 돈을 줄여준다.
'''
for i in range(len(juga)):
    if junMoney >= juga[i]:
        junStcok += junMoney // juga[i]
        junMoney %= juga[i]
'''
성민이는 
주가가 3일연속 떨어지면 '다음날' 주식을 사고
주가가 3일연속 오르면 '당일' 주식을 판다
그리고 성민이는 2일 뒤의 주가를 분석해야 하기 때문에
인덱스를 전부 순회하면 범위를 벗어나서 -3을 해줘야한다.
'''
for i in range(len(juga)-3):
    if juga[i] > juga[i+1] > juga[i+2]: # 주가가 계속 하락함
        sungStock += sungMoney // juga[i+3]
        sungMoney %= juga[i+3]
    elif juga[i] < juga[i+1] < juga[i+2]: # 주가가 계속 상승함
        sungMoney += sungStock * juga[i+2]
        sungStock = 0 #주식을 전량 매도하기 때문에 주식 보유량을 0으로 초기화 해줘야한다.
#마지막날 주가를 기준으로 돈을 계산하기 때문에 -1 으로 가장 마지막 주가를 곱해줬다
junMoney = (junStcok * juga[-1]) + junMoney
sungMoney = (sungStock * juga[-1]) + sungMoney

if junMoney > sungMoney:
    print("BNP")
elif junMoney < sungMoney:
    print("TIMING")
else:
    print("SAMESAME")