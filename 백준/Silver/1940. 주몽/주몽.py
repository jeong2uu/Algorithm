import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())


def mydef(N, M):
    count = 0
    # T = list(map(int,input().split()) for _ in range(N))
    T = list(map(int,input().split()))

    for i in range(len(T)):
        for j in range(i+1, len(T)):
            if T[i] + T[j] == M:
                count += 1
        
    print(count)



if __name__ == '__main__':
    mydef(N, M)