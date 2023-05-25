def solution(A):
    # given an array of length N
    # distinct integers within the range (1, N+1)
    # => one number is missing, find it!
    N = len(A)
    A.sort()

    # iterate over array
    print(A)
    for i in range(N):
        print (A[i+1], A[i])
        compare = A[i+1] - A[i]
        if not compare == 1:
            number = A[i]
            return number+1
A = [1,4,3,5,6,7,9,8,10,2,12]
print(solution(A))
