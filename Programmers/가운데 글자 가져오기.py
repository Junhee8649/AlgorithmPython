def solution(s):
    L = len(s)
    l = L // 2
    if L % 2 == 0:
        answer = s[l-1:l+1]
    else:
        answer = s[l]
    return answer