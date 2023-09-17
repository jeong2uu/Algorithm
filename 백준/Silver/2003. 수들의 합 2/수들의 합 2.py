def mydef():
    # print("n, m을 입력하세요: ")
    N, M = map(int, input().split())
    # print("list값을 입력하세요: ")
    A = list(map(int, input().split()))
    # print(A)
    
    count = 0
    for i in range(N):
        arrsum = 0
        for j in range(i, N):
            arrsum += A[j]
            if arrsum > M:     
                break
            elif arrsum == M:       # A[i] + A[i+1] + … + A[j-1] + A[j] == M
                count += 1
                break
    print(count)
    
if __name__ == '__main__':
    mydef()