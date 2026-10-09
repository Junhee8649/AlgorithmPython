from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque()
    q.append((0,0))
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1 and maps[nr][nc] == 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist[-1][-1]
