from collections import deque

n, m = map(int, input().split())

spot = deque()      # 주차 자리
weight = deque()    # 차량무게
wait = deque()  # 대기차량
use = [0] * n   # 사용중인 차량
total = 0

for i in range(n):                      
    spot.append(int(input().strip()))
for i in range(m):                      
    weight.append(int(input().strip()))   
for i in range(m*2):
    car = int(input().strip())
    if car > 0:
        if 0 in use:
            for j in range(n):
                if use[j] == 0:     # 주차자리 배당
                    use[j] = car
                    break
        else:
            wait.append(car)        # 대기 차량
    else:
        a = use.index(-car)         # 주차 차량이 모두 주차후 출차한 뒤
        use[a] = 0
        total+=weight[-car-1]*spot[a]
        if wait:
            use[a] = wait.popleft()

print(total)