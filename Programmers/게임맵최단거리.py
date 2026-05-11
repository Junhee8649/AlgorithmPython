from collections import deque


def solution(maps):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    N, M = len(maps), len(maps[0])
    q = deque()
    dist = [[-1] * M for _ in range(N)]
    q.append((0,0))
    dist[0][0] = 1

    while q:
        r, c = q.popleft()
        if (r, c) == (N-1, M-1):
            break
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    answer = dist[N-1][M-1]
    return answer