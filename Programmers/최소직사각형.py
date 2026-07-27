def solution(sizes):
    max_one, max_two = 0, 0
    for size in sizes:
        temp_one = max(size)
        max_one = max(temp_one, max_one)
        temp_two = min(size)
        max_two = max(temp_two, max_two)
    return max_one * max_two