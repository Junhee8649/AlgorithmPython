from collections import deque

def confirm(s):
    q = deque()
    for i in range(len(s)):
        if q:
            if q[-1] == '(' and s[i] == ')':
                q.pop()
                continue
            elif q[-1] == '[' and s[i] == ']':
                q.pop()
                continue
            elif q[-1] == '{' and s[i] == '}':
                q.pop()
                continue
        q.append(s[i])
    if q:
        return False
    else:
        return True
        

def solution(s):
    result = 0
    for i in range(len(s)):
        temp = confirm(s)
        if temp:
            result += 1
        s = s[1:] + s[:1]
    return result