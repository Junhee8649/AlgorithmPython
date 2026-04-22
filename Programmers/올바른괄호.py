from collections import deque


def solution(s):
    q = deque()
    
    for i in s:
        q.append(i)
        if len(q) >= 2 and q[-2] == '(' and q[-1] == ')':
            q.pop()
            q.pop()
    if q:
        return False
    else:
        return True