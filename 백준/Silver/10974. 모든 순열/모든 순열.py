import itertools
def permutation(N):
    nums = list(range(1, N+1))
    # print(nums)

    permute = list(itertools.permutations(nums))
    # print(permute)

    for permutes in permute:
        print(' '.join(str(perNum) for perNum in permutes))

if __name__ == '__main__':
    permutation(int(input()))