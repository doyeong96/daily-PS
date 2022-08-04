'''
합에 합을 더한다
1,2,3,4,5
1+2 = 3
ghap=3
ghap+3 = 6
'''

# n = 5
# num =[3, 1, 4, 3, 2]
n = int(input())
num = list(map(int,input().split()))
ghap = 0
hap = [] #합들을 넣어줄 리스트
num.sort() #인출 속도가 빠른 사람부터 인출해야 하기 때문에

for i in range(n):
    ghap += num[i]
    hap.append(ghap)
print(sum(hap))