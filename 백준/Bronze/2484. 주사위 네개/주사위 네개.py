
from sys import stdin
from collections import Counter

N = int(stdin.readline())
money = []

for i in range(N):
    prizeMoney = 0
    nums = Counter(stdin.readline().split())
    keylist = sorted(list(nums.keys()))
    vallist = sorted(list(nums.values()))

    if len(keylist) == 1:       # 모든 눈의 수가 같은 경우
        key = int(keylist[0])
        prizeMoney = 50000 + key * 5000
    
    elif len(keylist) == 2:      
        if 2 in vallist:            # 눈의 개수가 2쌍이 있는 경우(2266),
            for key in keylist:
                prizeMoney += int(key) * 500
            prizeMoney += 2000
        else:                       #눈의 개수가 3개가 같은 경우(3336)
            for k,v in nums.items():
                if v == 3:
                    key = int(k)
            prizeMoney = 10000 + key * 1000
            
    elif len(keylist) == 3:     # 눈의 개수가 2개가 같은 경우(1233)
        for k,v in nums.items():
            if v == 2:
                key = int(k)
        prizeMoney = 1000 + key * 100

    else:                       # 눈의 수가 모두 다른 경우(1256)
        maxkey = int(keylist[-1])
        prizeMoney = maxkey * 100
        
    money.append(prizeMoney)

print(max(money))