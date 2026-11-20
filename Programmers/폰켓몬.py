def solution(nums):
    N = len(nums) // 2
    n = len(set(nums))
    return n if n <= N else N 