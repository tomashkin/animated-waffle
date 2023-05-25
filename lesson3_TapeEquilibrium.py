def solution(A):

    N = len(A)
    sums = []

    for p in range(N):
        left = A[:p]
        right = A[p + 1:]
        calc = abs(sum(left) - sum(right))
        sums.append(calc)

    return min(sums)
