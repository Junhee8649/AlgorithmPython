from collections import deque

def solution(s):
    q = deque()
    
    for char in s:
        if q and q[-1] == char:
            q.pop()
        else:
            q.append(char)
            
    if not q:
        return 1
    else:
        return 0