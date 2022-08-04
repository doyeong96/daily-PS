'''
    1 도시 갯수 n
    2 도시 간 길이 n-1
    3 각 도시의 기름값 => 리스트에 넣음

    3번에서 마지막 도시의 기름값은 제외 => 어차피 마지막엔 기름을 넣지않음
'''

# n = int(input()) 
# dosi = list(map(int,input().split()))
# girum = list(map(int,input().split())) 
# girum = girum[:len(girum)-1] # 마지막 도시에서는 기름을 넣지 않기 때문에 마지막 도시의 기름값을 제외해준다
# price = 0
# dosisum = sum(dosi) #총 주행거리

# for i in range(n-1):
#     if dosisum == 0: # 가야하는 주행거리가 남아있지 않으면
#         print(price) # 가격을 출력하고 종료
#         break
#     if girum[i] != min(girum): #기름값[i]가 최소값이 아니면
#         price += girum[i]*dosi[i]  #price에 i번째 가격 * 주행거리를 넣어주고
#         dosisum -= dosi[i]  #총 주행거리에서 현재 주행거리를 빼준다
#     else: #최소값이면
#         price += girum[i]*dosisum #현재 가격*남은 주행거리를 전부 곱해주고
#         dosisum = 0 #주행거리를 0으로 초기화

n = int(input())
dosi = list(map(int,input().split())) #도시 거리
girumgap = list(map(int,input().split())) #도시 기름값
price = dosi[0] * girumgap [0] #어차피 처음에는 주유하기 때문에

# dosi = dosi[1:]
# girumgap = girumgap[1:len(girumgap)-1]

mingap = girumgap[0]


for i in range(1,n-1): #0번값은 이미 계산됐기 때문에 1번 인덱스 부터 시작
    if mingap < girumgap[i]: #첫번째 기름값이 가장 싼 경우
        price += mingap*dosi[i] #기름값은 변하지 않고 모든 km를 곱한다
    else: #첫번째 기름값이 가장 싸지 않다면
        mingap = girumgap[i] #mingap 를 i번(1번) 인덱스의 기름값으로 바꾸어주고
        price += mingap*dosi[i] # 가격에 mingap*dosi[i(1)] 를 더해준다
print(price)


