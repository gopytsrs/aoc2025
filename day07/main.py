from collections import deque

def parse():
    with open("data.in", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return r, c


def solve1():
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    sr, sc = find_start(grid)

    queue = deque([(sr, sc)])
    visited = set([(sr, sc)])
    splits = 0

    while queue:
        r, c = queue.popleft()
        if r + 1 >= ROWS:
            continue
        below = grid[r + 1][c]
        if below == ".":
            if (r + 1, c) not in visited:
                visited.add((r + 1, c))
                queue.append((r + 1, c))
        elif below == "^":
            splits += 1
            if c - 1 >= 0 and (r + 1, c - 1) not in visited:
                visited.add((r + 1, c - 1))
                queue.append((r + 1, c - 1))
            if c + 1 < COLS and (r + 1, c + 1) not in visited:
                visited.add((r + 1, c + 1))
                queue.append((r + 1, c + 1))
    return splits

def solve2():
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    sr, sc = find_start(grid)

    dp = [[0] * COLS for _ in range(ROWS)]
    dp[sr][sc] = 1

    for r in range(sr, ROWS - 1):
        for c in range(COLS):            
            below = grid[r + 1][c]
            if below == '.':
                dp[r + 1][c] += dp[r][c]
            elif below == '^':
                if c - 1 >= 0:
                    dp[r + 1][c - 1] += dp[r][c]
                if c + 1 < COLS:
                    dp[r + 1][c + 1] += dp[r][c]

    return sum(dp[ROWS-1][c] for c in range(COLS))

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")