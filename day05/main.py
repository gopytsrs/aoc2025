def parse():
    with open("data.in", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        ranges = []
        i = 0
        while i < len(lines):
            if lines[i] == '':
                break
            start, end = lines[i].split('-')
            ranges.append((int(start), int(end)))
            i += 1
        i += 1
        available = []
        while i < len(lines):
            available.append(int(lines[i]))
            i += 1
        return ranges, available

def merge_ranges(ranges):
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])  
    return merged


def solve1():
    ranges, available = parse()
    ranges.sort()
    merged = merge_ranges(ranges)
    fresh = 0
    for ingredient in sorted(available):
        for start, end in merged:
            if start <= ingredient <= end:
                fresh += 1
                break
    return fresh

def solve2():
    ranges, _ = parse()
    ranges.sort()
    merged = merge_ranges(ranges)
    fresh = 0
    for start, end in merged:
        fresh += end - start + 1
    return fresh

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")