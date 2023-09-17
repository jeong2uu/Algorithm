from sys import stdin 

T = int(stdin.readline())
txt = list(stdin.readline())

for _ in range(T-1):
    txt2 = stdin.readline()
    for i in range(len(txt)):
        if txt[i] != txt2[i]:
            txt[i] = "?"
        else:
            continue

print(*txt, sep = "")