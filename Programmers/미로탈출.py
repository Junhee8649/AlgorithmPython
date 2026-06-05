from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    result = 0
    N, M = len(maps), len(maps[0])
    map = []
    for i in maps:
        temp = []
        for j in i:
            temp.append(j)
        map.append(temp)
        
    q = deque()
    dist = [[-1] * M for _ in range(N)]
    is_pull = False
    is_finish = False
    
    for i in range(N):
        for j in range(M):
            if map[i][j] == 'S':
                q.append((i, j))
                dist[i][j] = 0
                break
    while q:
        y, x = q.popleft()
        if map[y][x] == 'L':
            result += dist[y][x]
            q.clear()
            dist = [[-1] * M for _ in range(N)]
            dist[y][x] = 0
            is_pull = True
        if map[y][x] == 'E' and is_pull:
            result += dist[y][x]
            is_finish = True
            break
            
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and map[ny][nx] != 'X' and dist[ny][nx] == -1:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
    if is_finish:
        return result
    else:
        return -1