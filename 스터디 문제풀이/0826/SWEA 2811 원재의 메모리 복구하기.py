'''
각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다.
원래 메모리에서 1이나오면 체크 
1을 체크한 후에 0이 나오면 다시 체크

원래 메모리의 앞 뒤 값이 다르면 1증가
첫번째 메모리가 1으로 시작하면 카운트를 1부터 시작
'''

for test in range(int(input())):
    memory = list(input()) # 원래 메모리
    n = len(memory)
    cnt = 0
    if memory[0] == '1':
        cnt = 1
    for i in range(n - 1):
        if memory[i] != memory[i+1]:
            cnt += 1
    # print(n)
    print(f'#{test + 1} {cnt}')
    # print(n)
    # print(memory)
    # bit = [0] * n
    # print(bit)
