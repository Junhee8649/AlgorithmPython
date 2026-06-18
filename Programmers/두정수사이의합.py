def solution(a, b):
    a, b = min(a, b), max(a, b)
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer