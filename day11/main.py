from collections import defaultdict

def parse():
    graph = defaultdict(list)
    with open("data.in", 'r') as f:
        for line in f.readlines():
            source, rest = line.strip().split(':')
            destinations = rest.strip().split()
            graph[source].extend(destinations)
    return graph

def solve1():
    graph = parse()
    memo = {}
    
    def dfs(curr):
        if curr == 'out':
            return 1
        if curr in memo:
            return memo[curr]
        memo[curr] = 0
        for nei in graph[curr]:
            memo[curr] += dfs(nei)
        return memo[curr]

    return dfs("you")

def solve2():
    graph = parse()
    memo = {}
    
    def dfs(curr, dac_visited, fft_visited):
        if curr == "out":
            return int(dac_visited and fft_visited)
        if (curr, dac_visited, fft_visited) in memo:
            return memo[(curr, dac_visited, fft_visited)]
        memo[(curr, dac_visited, fft_visited)] = 0
        for nei in graph[curr]:
            memo[(curr, dac_visited, fft_visited)] += dfs(
                nei, 
                dac_visited or (nei == "dac"), 
                fft_visited or (nei == "fft")
            )
        return memo[(curr, dac_visited, fft_visited)]

    return dfs("svr", False, False)


print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")