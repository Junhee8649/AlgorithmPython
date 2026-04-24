import math

def solution(n):
    # 카탈랑 수 활용 -> 2nCn * n+1분의 1
    return math.comb(2 * n, n) // (n + 1)