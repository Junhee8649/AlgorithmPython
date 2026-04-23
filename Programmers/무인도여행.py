from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    map = []
    for i in maps:
        temp = []
        for j in i:
            if j != 'X':
                temp.append(int(j))
            else:
                temp.append(j)
        map.append(temp)
    
    q = deque()
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if map[i][j] != 'X' and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                temp_distance = map[i][j]
                while q:
                    y, x = q.popleft()
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and map[ny][nx] != 'X':
                            q.append((ny, nx))
                            temp_distance += map[ny][nx]
                            visited[ny][nx] = True
                answer.append(temp_distance)
    answer.sort()
    if not answer:
        answer.append(-1)

    return answer