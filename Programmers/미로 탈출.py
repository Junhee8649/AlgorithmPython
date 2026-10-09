from collections import deque


def solution(maps):
    N, M = len(maps), len(maps[0])
    def bfs(sijak, dochak):
        dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
        sijak_r, sijak_c = sijak
        dochak_r, dochak_c = dochak
        q = deque([(sijak_r, sijak_c, 0)])
        visited = [[False] * M for _ in range(N)]
        visited[sijak_r][sijak_c] = True
        
        while q:
            r, c, t = q.popleft()
            if (r, c) == (dochak_r, dochak_c):
                return t
            
            for d in range(4):
                nr, nc, nt = r + dr[d], c + dc[d], t + 1
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    q.append((nr, nc, nt))
        return -1

    start = lever = end = (0, 0)
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'O' and maps[i][j] != 'X':
                if maps[i][j] == 'S':
                    start = (i, j)
                elif maps[i][j] == 'L':
                    lever = (i, j)
                else:
                    end = (i, j)
    lever_time = bfs(start, lever)
    exit_time = bfs(lever, end)

    if lever_time == -1 or exit_time == -1:
        return -1
    else:
        return lever_time + exit_time