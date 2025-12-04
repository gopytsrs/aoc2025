from collections import defaultdict, deque

def parse():
    with open("data.in", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def next_cells(r, c, ROWS, COLS):
    for nr, nc in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                   (r, c - 1), (r, c + 1),
                   (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)):
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc

def solve1():
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != '@':
                continue
            surrounding = sum(grid[nr][nc] == '@' for nr, nc in next_cells(r, c, ROWS, COLS))
            result += 1 if surrounding < 4 else 0
    return result

def solve2():
    grid = parse()
    ROWS, COLS = len(grid), len(grid[0])
    graph = defaultdict(set)
    indegree = defaultdict(int)
    cells = set()
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != '@':
                continue
            for nr, nc in next_cells(r, c, ROWS, COLS):
                if grid[nr][nc] != '@':
                    continue
                graph[(r, c)].add((nr, nc))
                indegree[(r, c)] += 1
            cells.add((r, c))
    
    queue = deque([cell for cell in cells if indegree[cell] < 4])
    removable = set([cell for cell in cells if indegree[cell] < 4])
    while queue:
        cell = queue.popleft()
        for next_cell in graph[cell]:
            indegree[next_cell] -= 1
            if indegree[next_cell] < 4 and next_cell not in removable:
                removable.add(next_cell)
                queue.append(next_cell)
    return len(removable)

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
        
