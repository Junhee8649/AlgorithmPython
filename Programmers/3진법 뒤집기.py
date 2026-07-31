def to_ternary(n):
    if n == 0:
        return '0'
    res = []
    while n:
        n, rem = divmod(n, 3)
        res.append(str(rem))
    return ''.join(res)

def solution(n):
    temp = to_ternary(n)
    return int(temp, 3)