from sys import stdin 
from collections import Counter

a, b = Counter(stdin.readline().strip()), Counter(stdin.readline().strip())
# print(a-b) # Counter({'a': 2, 'c': 2})
# print(b-a) # Counter({'x': 2, 'y': 2})
print(sum((a-b).values()) + sum((b-a).values()))