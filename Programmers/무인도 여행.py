from collections import deque

def solution(maps):
    answer = []
    dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
    N, M = len(maps), len(maps[0])
    new_map = []
    
    for m in maps:
        temp = []
        for k in m:
            temp.append(k)
        new_map.append(temp)
    
    visited = [[False] * M for _ in range(N)]
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if new_map[i][j] != 'X' and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                food = int(new_map[i][j])
                
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and new_map[nr][nc] != 'X':
                            food += int(new_map[nr][nc])
                            visited[nr][nc] = True
                            q.append((nr, nc))
                answer.append(food)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer
                        