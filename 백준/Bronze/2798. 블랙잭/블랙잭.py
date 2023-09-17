from itertools import combinations
from sys import stdin

N, M = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))
result = []

com = list(combinations(card, 3))

for comNum in com:
    sum = comNum[0] + comNum[1] + comNum[2]
    if sum <= M:
        result.append(sum)

print(max(result))