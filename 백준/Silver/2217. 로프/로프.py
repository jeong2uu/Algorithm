from sys import stdin 

N = int(stdin.readline())
loops = [int(stdin.readline()) for _ in range(N)]
max = 0

loops.sort(reverse=True)
# print(loops)

for n in range(1,N+1):
    w = loops[n-1] * n
    if max < w:
        max = w

print(max)