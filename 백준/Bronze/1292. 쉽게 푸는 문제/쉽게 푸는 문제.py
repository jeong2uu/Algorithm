from sys import stdin
from unittest import result

A, B = map(int, stdin.readline().split())

nums = []
integer = 1
result = 0

for i in range(1000):
    for num in range(i+1):
        nums.append(integer);
    integer += 1

for j in range(A-1,B):
    # print(nums[j])
    result += nums[j]

print(result)