'''준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.'''
'''
    n 동전의 종류
    k 동전을 사용해서 만들 가치합
    cnt 동전이 몇개 필요한지

    입력한 동전을 하나의 리스트에 담는다
    내림차순으로 정렬한다
    for 문을 돌려서 k값과 비교한다
    k값보다 크면 넘어간다
    k값보다 작으면
    k//n 해서 몫을 cnt 에 담는다
    k = k%n 으로 나머지를 k에 넣는다(k 값이 줄어드는것)
    k가 0이 되면 종료 while k != 0 k가 0이 아닐때만 반복
'''

# n, k = map(int,input().split())
# num = []
# # num = num.append(int,input().split())

# num = [1,5,10,50,100,500,1000,5000,10000,50000]
# k = 4200

# # for i in range(n):
# #     num = num.append(int(input()))

# num = sorted(num,reverse=True)
# cnt = 0
# while k != 0:
#     for i in num:
#         if i < k:
#             cnt += k//i
#             k = k%i
#         else:
#             continue
# # for i in n:
# #     print(i)
# print(cnt)

#n ,k 를 나눠서 할당
n,k = map(int,input().split())
#가치를 담을 빈 리스트
num = []

#for문을 돌면서 가치를 하나씩 받고 num에 담아줌
for i in range(n):
    num.append(int(input()))

#내림차순 정렬
num = sorted(num,reverse=True)
cnt = 0

# k가 0이되면 와일문 탈출
# 리스트에 담긴 숫자를 하나씩 빼서 i에 담는다
# 만약 i값보다 k값이 크다면
# 몫을 cnt에 담고 
# 나머지를 k 에 담아서 숫자를 줄여나간다
# 근데 이거 실패함 왜지?

# while k != 0:
#     for i in num:
#         if i < k:
#             cnt += k//i
#             k = k % i
# print(cnt)


#가치를 한번씩 돌면서 
#몫을 cnt에 담아주고 
#나머지를 k 에 담아서 숫자를 점점 줄여나간다.
for i in num:
    cnt += k//i
    k = k % i
print(cnt)