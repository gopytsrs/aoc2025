def parse():
    with open("data.in", "r") as f:
        return [list(map(int, list(line.strip()))) for line in f.readlines()]

def get_max_value(line, seq_len):
    
    memo = {}
    
    def dfs(i, curr_len):
        if i < 0:
            if curr_len != seq_len:
                return float("-inf")
            return 0
        if (i, curr_len) in memo:
            return memo[(i, curr_len)]
        skip = dfs(i - 1, curr_len)
        use = dfs(i - 1, curr_len + 1) * 10 + line[i]
        memo[(i, curr_len)] = max(skip, use)
        return memo[(i, curr_len)]

    return dfs(len(line) - 1, 0)

def solve1():
    return sum(get_max_value(line, 2) for line in parse())

def solve2():
    return sum(get_max_value(line, 12) for line in parse())

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")