def solution(s):
    if s[0] != '-':
        answer = int(s)
    else:
        answer = -int(s[1:])
    return answer