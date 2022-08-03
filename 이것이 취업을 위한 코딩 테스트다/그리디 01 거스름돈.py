money = int(input())
# money = 1260
coins =[500,100,50,10]
coins =sorted(coins,reverse=True)
count = 0

while money != 0:
    if money > coins[0]:
        count += money//coins[0]
        money = money%coins[0]
    elif money > coins[1]:
        count += money//coins[1]
        money = money%coins[1]
    elif money > coins[2]:
        count += money//coins[2]
        money = money%coins[2]
    else:
        count += money//coins[3]
        money = money%coins[3]
print(count)


'''
    거스름돈 줄때 동전 최소갯수
    값이 큰 동전부터 준다
    거스름돈 정렬해서 큰것부터 줄수있게한다.
    몫 = 넘겨준 동전갯수
    나머지 = 남은 거스름돈

    근데 동전이 5개면?
'''

'''
    교재 답안

for coin in coins:
    count += money // coin
    money = money%coin
print(count)
'''
