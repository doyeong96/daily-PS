'''
    최솟값 찾기, -값을 키우는게 핵심

    첫번째 입력에 식을 넣어준다
    '-'를 기준으로 나눠준다. => 리스트로 값이 들어온다


    어차피 맨 앞의 식[0] (-를 만나기 전) 은 +이기 때문에 다 더한다
    +기준으로 나눠서 숫자가 되게한다
    dap += 으로 넣어준다

    식[1:]도 결국 ()안은 +이기 때문에 다 더한다
    +기준으로 나눠서 숫자가 되게한다
    괄호를 벗어나면 -를 만나기때문에 -=으로 값을 빼준다




    리스트로 하지말자 어려움 못하겠음
    sum()를 통해서 각 리스트의 합을 구해주고
    전부 뺀다 list[i]-list[i+1]을 반복하고 변수에 할당 혹은 리스트에 넣고 다시 sum
'''

nums = input().split('-') #식을 입력받는다
hap1 = 0 # -를 만나기 전 숫자들의 합
hap2 = 0 # -를 만난 후 숫자들의 합

# dap = sum(num[0])
# print(nums)

# print(nums[1:])
for i in map(int,nums[0].split('+')): #-를 만나기 전 숫자들은 nums[0]
    hap1 += i

for i in nums[1:]: # - 이후의 숫자들은 어차피 쭉 - 이므로
    # i = list(map(int,i.split('+'))) # 연산자를 신경쓰지 않고 리스트에 담아준 뒤
    # hap2 = (sum(i)) # 합계를 구하고
    for j in map(int,i.split('+')):
        hap2 -= j
dap = hap1 + hap2 #처음 합과 이후 합을 빼준다
print(dap)

# print(hap1)


# nums = input().split('-')
# hap1 = 0
# hap2 = 0

# for i in map(int,nums[0].split('+')):
#     hap1 += i

# for i in nums[1:]:
#     i.split('+')
#     hap2 -= i

# dap = hap1 + hap2
# print(dap)