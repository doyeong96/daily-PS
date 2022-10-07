for test in range(int(input())):
    s = 0
    e = int(input())
    mid = (s + e) // 2
    wordL = list(map(str, input().split()))
    Lword = []
    Rword = []
    suffle = []
    if e % 2: # 홀짝 처리
        for i in range(s, mid+1):
            Lword.append(wordL[i])
        for j in range(mid+1, e):
            Rword.append(wordL[j])
    else:
        for i in range(s, mid):
            Lword.append(wordL[i])
        for j in range(mid, e):
            Rword.append(wordL[j])
    while len(suffle) != e:
        suffle.append(Lword.pop(0))
        if len(Rword) == 0: # 왼쪽 단어 리스트는 무조껀 오른쪽 단어 리스트보다 많음
            pass
        else:
            suffle.append(Rword.pop(0))
    print(f'#{test+ 1 }', end=' ')
    print(*suffle)