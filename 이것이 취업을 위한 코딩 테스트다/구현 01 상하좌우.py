n = int(input())
move = list(map(str, input().split()))
direction = [1, 1]
'''
크기가 5일때
기본 위치를 [i,j] 로 할때
    l = j-1 => 
    r = j+1
    u = i-1
    d = i+1
    
공간 밖으로 벗어 나지 않게 해야함
l 일때 j가 1보다 클때만 => direction[1] 이 2는 돼야 왼쪽으로 갈수있음
r 일때 j가 5(n)보다 작을때만
u 일때 i가 1보다 클때만
d 일때 i가 5(n)보다 작을때만
이동 가능 
'''
for i in move:
    if i == 'L':
        if direction[1] > 1:
            direction[1] -= 1
    elif i == 'R':
        if direction[1] < n:
            direction[1] += 1
    elif i == 'U':
        if direction[0] > 1:
            direction[0] -= 1
    else:
        if direction[0] < n:
            direction[0] += 1

print(direction[0], direction[1])
