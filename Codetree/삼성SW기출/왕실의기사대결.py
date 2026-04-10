from collections import deque

# L x L 크기, N명의 초기 기사, Q번의 명령
L, N, Q = map(int, input().split())
chess_grid = [list(map(int, input().split())) for _ in range(L)]
# 좌측상단 (r, c), 높이 h, 너비 w, 체력 k
warriors = [list(map(int, input().split())) for _ in range(N)]
original_warriors_heart = []
for i in warriors:
    original_warriors_heart.append(i[4])
warriors_grid = [[0] * L for _ in range(L)]
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def place_warriors():
    for warrior in range(N):
        r,c,h,w,k = warriors[warrior]
        for i in range(r-1, r+h-1):
            for j in range(c-1, c+w-1):
                warriors_grid[i][j] = warrior+1

def move(i, d):
    mr, mc, mh, mw, mk = warriors[i-1]
    if mk <= 0:
        return
    moving = {i}
    q = deque()
    q.append((mr, mc, mh, mw))
    
    # 연쇄적으로 움직이는 모든 기사 moving에 넣기
    while q:
        mr, mc, mh, mw = q.popleft()
        for r in range(mr-1, mr+mh-1):
            for c in range(mc-1, mc+mw-1):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < L and 0 <= nc < L and warriors_grid[nr][nc] != 0:
                    num = warriors_grid[nr][nc]
                    if num not in moving:
                        moving.add(num)
                        q.append((warriors[num-1][0], warriors[num-1][1], warriors[num-1][2], warriors[num-1][3]))

    isavailable = True
    for temp in moving:
        tr, tc, th, tw, tk = warriors[temp-1]
        for r in range(tr-1, tr+th-1):
            for c in range(tc-1, tc+tw-1):
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < L and 0 <= nc < L) or chess_grid[nr][nc] == 2:
                    isavailable = False


    if isavailable:
        moving_available = []
        for r in range(L):
            for c in range(L):
                if warriors_grid[r][c] in moving:
                    moving_available.append((r, c, warriors_grid[r][c]))
        if d == 0:
            moving_available.sort(key=lambda x: x[0])
        elif d == 1:
            moving_available.sort(key=lambda x: -x[1])
        elif d == 2:
            moving_available.sort(key=lambda x: -x[0])
        elif d == 3:
            moving_available.sort(key=lambda x: x[1])
        
        for r, c, num in moving_available:
            nr, nc = r + dr[d], c + dc[d]
            warriors_grid[nr][nc] = num
            warriors_grid[r][c] = 0
        for a in moving:
            warriors[a-1][0] += dr[d]
            warriors[a-1][1] += dc[d]
        moving.remove(i)
        return moving
    else:
        return

def fight(moving):
    for i in range(L):
        for j in range(L):
            num = warriors_grid[i][j]
            if num in moving and chess_grid[i][j] == 1:
                warriors[num-1][4] -= 1
                if warriors[num-1][4] == 0:
                    tr, tc, th, tw, _ = warriors[num-1]
                    for r in range(tr-1, tr+th-1):
                        for c in range(tc-1, tc+tw-1):
                            warriors_grid[r][c] = 0


def all_live_damage():
    damage = 0
    for i in range(N):
        if warriors[i][4] >= 1:
            damage += (original_warriors_heart[i] - warriors[i][4])
    print(damage)


warriors_grid = [[0] * L for _ in range(L)]
place_warriors()
for _ in range(Q):
    # i번 기사에게 d로 이동
    i, d = map(int, input().split())
    moving = move(i, d)
    if moving:
        fight(moving)
all_live_damage()