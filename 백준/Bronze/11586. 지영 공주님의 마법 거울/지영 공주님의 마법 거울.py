from sys import stdin

N = int(stdin.readline())
strlist = [list(stdin.readline().strip()) for _ in range(N)]
mindNum = int(stdin.readline())

# 1일 때는 지영 공주님의 모습을 있는 그대로 표현하고, 2일 때는 좌/우로 반전된 모습을, 3일 때는 상/하로 반전된 모습을 표현
if mindNum == 1:
    for lst in strlist:
        print(''.join(lst))
elif mindNum == 2:
    for lst in strlist:
        rowlst = list(reversed(lst))
        print(''.join(rowlst))
else:
    updownlst = list(reversed(strlist))
    for lst in updownlst:
        print(''.join(lst))