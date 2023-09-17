from sys import stdin

S = ["STRAWBERRY", "BANANA", "LIME", "PLUM"]
count = [0]*len(S)
result = False

N = int(stdin.readline())

for idx in range(N):
    card, X = map(str, stdin.readline().split())

    if card == S[0]:
        count[0] += int(X)
    elif card == S[1]:
        count[1] += int(X)
    elif card == S[2]:
        count[2] += int(X)
    else:
        count[3] += int(X)
    
for time in count:
    if time == 5:
        result = True
    
if result == True:
    print("YES")
else:
    print("NO")

