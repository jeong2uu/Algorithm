from sys import stdin, maxsize

C, N = map(int, input().split())    # city, city count
Ad = [list(map(int, stdin.readline().split())) for _ in range(N)] # [cost, customor]
dp = [0] + [maxsize] * (C + 100)

# print(dp)

for cost, customer in Ad:
        for cur_customer in range(customer, C + 101):
            dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)
            # dp[N명의 고객을 유치하는데 드는 비용] = min(dp[N명의 고객을 유치하는데 드는 비용], dp[N명의 고객을 유치하는데 드는 비용 - 현재 방문한 도시의 유치 가능한 인원수) + cost)
    
print(min(dp[C:C + 101]))