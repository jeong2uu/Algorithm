from sys import stdin

N = int(stdin.readline())
zero = []

for n in range(N):
    num = int(stdin.readline())
    
    if num != 0:
        zero.append(num)
    else:
        zero.pop()

result = sum(zero)
print(result)

