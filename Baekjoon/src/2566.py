grid = [list(map(int, input().split())) for _ in range(9)]
max = 0
max_coords = (1, 1)
for i in range(9):
    for j in range(9):
        if grid[i][j] > max:
            max = grid[i][j]
            max_coords = (i + 1, j + 1)
print(max)
print(*max_coords)
