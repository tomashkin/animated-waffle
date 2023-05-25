import math


def solution(X, Y, D):
    dist = Y-X
    # here we use an implementation of ceiling division
    # the // operator is floor division. By modifying as follows, we attain ceiling division.
    #
    jumps = math.ceil(dist/D)
    return jumps

print(solution(10, 50, 17))