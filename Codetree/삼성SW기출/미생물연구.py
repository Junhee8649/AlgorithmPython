from collections import deque

# N x N 크기랑 Q번의 횟수 
N, Q = map(int, input().split())
microbe_list = [list(map(int, input().split())) for _ in range(Q)]
grid = [[-1] * N for _ in range(N)]
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def insert(r1,c1,r2,c2,microbe_num):
    for i in range(r1, r2):
        for j in range(c1, c2):
            grid[i][j] = microbe_num

# 갈라진 무리 탐색해주는 함수 (BFS)
def check_split():
    mass_count = [0] * Q
    visited = [[False] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if grid[i][j] != -1 and not visited[i][j]:
                num = grid[i][j]
                q.append((i,j))
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == num:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                mass_count[num] += 1
    for i in range(N):
        for j in range(N):
            num = grid[i][j]
            # 빈 칸이 아니고, 해당 미생물 번호의 덩어리가 2개 이상
            if num != -1 and mass_count[num] > 1:
                grid[i][j] = -1 # 


def move():
    # 1. 정보 수집
    groups = [[] for _ in range(Q)] 
    for i in range(N):
        for j in range(N):
            num = grid[i][j]
            if num != -1:
                groups[num].append((i, j))
    # 2. 살아남은 미생물 번호만 추려서 우선순위 정렬하기
    survivors = [num for num in range(Q) if groups[num]]
            
    # 정렬 기준: 면적(좌표 개수)은 내림차순(-), 번호는 오름차순(+) 정렬
    survivors.sort(key=lambda x: (-len(groups[x]), x))
    
    # 3 & 4. 새 용기에 배치 (상대 좌표 활용)
    new_grid = [[-1] * N for _ in range(N)]
    
    for num in survivors:
        coords = groups[num]
        ref_r, ref_c = coords[0] # 첫 번째 칸을 기준점(0, 0)으로 삼음
        
        placed = False
        # (i, j) 위치에 기준점을 맞췄을 때 배치할 수 있는지 검사
        for i in range(N):
            for j in range(N):
                can_place = True
                
                # 도장이 다 찍히는지 꼼꼼히 확인
                for r, c in coords:
                    nr = i + (r - ref_r) # 실제 놓일 x 좌표
                    nc = j + (c - ref_c) # 실제 놓일 y 좌표
                    
                    # 격자 범위를 벗어나거나, 이미 다른 미생물이 자리 잡고 있다면 실패!
                    if not (0 <= nr < N and 0 <= nc < N) or new_grid[nr][nc] != -1:
                        can_place = False
                        break
                
                # 무사히 모든 칸이 통과했다면 도장을 꾹 찍자!
                if can_place:
                    for r, c in coords:
                        nr = i + (r - ref_r)
                        nc = j + (c - ref_c)
                        new_grid[nr][nc] = num # 새 격자에 미생물 기록
                    
                    placed = True
                    break # 위치를 찾았으니 y 반복문(j) 탈출
            if placed:
                break # 위치를 찾았으니 x 반복문(i) 탈출
                
    # 5. 다 옮겼으니 기존 grid를 new_grid의 상태로 덮어쓰기
    for i in range(N):
        for j in range(N):
            grid[i][j] = new_grid[i][j]

def record():
    # 1. 넓이 구하기
    areas = [0] * Q
    for i in range(N):
        for j in range(N):
            num = grid[i][j]
            if num != -1:
                areas[num] += 1
                
    # 2. 인접한 쌍 찾기 (중복 방지를 위해 set 사용)
    adjacent_pairs = set()
    
    for i in range(N):
        for j in range(N):
            A = grid[i][j]
            if A == -1: # 빈칸이면 패스
                continue
                
            # 상하좌우 4방향 탐색
            for d in range(4):
                ni = i + dr[d]
                nj = j + dc[d]
                
                # 격자 범위 안이고, 빈칸이 아니며, 나와 다른 미생물이라면!
                if 0 <= ni < N and 0 <= nj < N:
                    B = grid[ni][nj]
                    if B != -1 and A != B:
                        # (작은 번호, 큰 번호) 형태로 만들어서 set에 쏙!
                        pair = (min(A, B), max(A, B))
                        adjacent_pairs.add(pair)
                        
    # 3. 점수 계산하기
    total_score = 0
    for A, B in adjacent_pairs:
        total_score += areas[A] * areas[B]
        
    print(total_score)


for i in range(Q):
    r1, c1, r2, c2 = microbe_list[i]
    insert(r1,c1,r2,c2,i)
    check_split()
    move()
    record()