'''
m*n
n행의 가장 작은 숫자 
중 가장 큰 숫자
'''

m, n = map(int,input().split())
minimum = []
#어차피 n번째 줄의 가장 작은 값을 찾으니까
for i in range(n):
    cards = list(map(int, input().split()))
    #작은 값을 minimum 에 넣는다
    minimum.append(min(cards))
    #그 중 가장 큰 값을 찾는다
    maxOfmin = max(minimum)
print(maxOfmin)