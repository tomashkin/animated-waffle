def solution(N):
    str = bin(N)
    new_str = str.lstrip('0b').rstrip('0')

    current_count = 0
    max_count = 0
    print(new_str)
    for i in new_str:
        if int(i) == 0:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

    # TODO figure out how to not look at the final binary gap
    # Try by checking at the final index, whether you are at a 0 or a 1 and then dont allow that current counter to be max counter
n = 32
print(n)
print(bin(n))
print(solution(n))