from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]: 
            q = deque([i])
            visited[i] = True
        
            while q:
                curr = q.popleft()
                for j in range(n):
                    if computers[curr][j] == 1 and not visited[j]:
                        q.append(j)
                        visited[j] = True
            answer += 1 

    return answer