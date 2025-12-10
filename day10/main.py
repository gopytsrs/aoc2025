from collections import deque
from z3 import Int, Optimize, Sum, sat

def parse():
    with open("data.in", 'r') as f:
        patterns = []
        joltage_reqs = []
        buttons_list = []
        for line in f.readlines():
            parts = line.strip().split()
            pattern = parts[0][1:-1]
            joltage_req = tuple(map(int, parts[-1][1:-1].split(',')))
            buttons = [tuple(map(int, part[1:-1].split(','))) for part in parts[1:-1]]
            patterns.append(pattern)
            joltage_reqs.append(joltage_req)
            buttons_list.append(buttons)
        return patterns, joltage_reqs, buttons_list

def get_masks(buttons, pattern):
    pattern_mask = 0
    for i, p in enumerate(pattern):
        if p == '#':
            pattern_mask |= (1 << i)
    
    button_masks = []
    for button in buttons:
        button_mask = 0
        for pos in button:
            button_mask |= (1 << pos)
        button_masks.append(button_mask)
    return button_masks, pattern_mask

def get_min_presses(button_masks, pattern_mask):
    queue = deque([(0, 0)])
    visited = set([0])
    while queue:
        curr_mask, curr_presses = queue.popleft()
        if curr_mask == pattern_mask:
            return curr_presses
        for button_mask in button_masks:
            new_mask = curr_mask ^ button_mask
            if new_mask in visited:
                continue
            visited.add(new_mask)
            queue.append((new_mask, curr_presses + 1))

def solve1():
    patterns, _, buttons_list = parse()
    result = 0
    for pattern, buttons in zip(patterns, buttons_list):
        button_masks, pattern_mask = get_masks(buttons, pattern)
        result += get_min_presses(button_masks, pattern_mask)
    return result

def get_min_presses_for_joltages(joltage, buttons):
    opt = Optimize()
    press_counts = [Int(f"c_{i}") for i in range(len(buttons))]

    for count in press_counts:
        opt.add(count >= 0)

    for pos, jol in enumerate(joltage):
        affects = [press_counts[i] for i, button in enumerate(buttons) if pos in button]
        opt.add(Sum(affects) == jol)
    opt.minimize(Sum(press_counts))

    if opt.check() == sat:
        model = opt.model()
        return sum(model[c].as_long() for c in press_counts)
    
def solve2():
    _, joltage_reqs, buttons_list = parse()
    result = 0
    for joltage, buttons in zip(joltage_reqs, buttons_list):
        result += get_min_presses_for_joltages(joltage, buttons)
    return result

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")