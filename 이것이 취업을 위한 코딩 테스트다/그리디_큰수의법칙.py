#큰수 반복
n, m, k= map(int,input().split())
# int(m)
# int(k)
# m = 8
# k = 3
numlist = list(map(int,input().split()))
# numlist = [2,4,5,4,6]
hap = 0
sumcount = 0
count = 0
sortednum = sorted(numlist,reverse=True)

while count != m:
    if sumcount <k:
        hap += sortednum[0]
        sumcount+=1
        count+=1
    else:
        hap += sortednum[1]
        sumcount = 0
        count+=1
print(hap)

'''
    입력된 배열값을 큰수부터 시작하게 정렬해준다.
        
    count 가 8이 아닐때까지 더해준다
    만약에 sumcount가 3보다 작으면 
    sortednum[0](가장 큰수) 를 더해주고
    sumcount,count 를 1씩 늘려준다
    3보다 커지면 sortednum[1](두번째 큰수)를 더해주고
    count는 1 증가시키고 sumcount 는 0으로 초기화한다

    count 가 8 이되면 종료하고 결과 반환
'''