'''
    n이 1이 될때까지 k를 가지고 계산함
    1번조건 n-1
    2번조건 n/k 단 n%k == 0 일때만
    while n != 1
'''

n,k = map(int,input().split())
count = 0
while n != 1:
    if n % k == 0:
        n/=k
        count+=1
    else:
        n-=1
        count+=1
print(count)
        