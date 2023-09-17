from sys import stdin

N, M = map(int,stdin.readline().split())
book = sorted(list(map(int, stdin.readline().split())))
# [-39, -37, -29, -28, -6, 2, 11]

# maxval = max(np.abs(book))
maxval = abs(book[0]) if abs(book[0]) > abs(book[-1]) else abs(book[-1])
min = []
plus = []
totalwalk = 0

for num in book:
    if num > 0:
        plus.append(num)
    else:
        min.append(num)

for m in range(0,len(min),M):
    if abs(min[m]) == maxval:
        pass
    else:
        totalwalk += abs(min[m])*2

plus.sort(reverse=True)
for p in range(0,len(plus),M):
    if plus[p] == maxval:
        pass
    else:
        totalwalk += plus[p]*2

print(totalwalk+maxval)
