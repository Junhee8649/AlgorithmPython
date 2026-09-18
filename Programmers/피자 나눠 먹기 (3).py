def solution(slice, n):
    if n % slice == 0:
        return n // slice
    return (n // slice) + 1