def solution(A, K):
    rotated_list = list()

    # make K modulo K, no point to rotate more that length of list
    if K == 0:
        pass
    elif K > 0:
        K = K % len(A)
    else:
        print('K out of range')
    N = len(A)
    for i in range(K):

        # do the first part
        rotated_list.append(A[N-K+i])


    for i in range(N-K):
        rotated_list.append(A[i])
    return rotated_list
A = [1, 2, 3, 4, 5, 6]

print(solution(A,1))
