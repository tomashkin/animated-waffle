def solution(A):
    values = set(A)
    print(values)

    for element in values:
        if A.count(element) % 2 == 1:
            return element

# this solution is simply written, but unfortunately time complex. Try again with an XOR
