def get_input():
    f = open("data.in")
    rotations = [line.strip() for line in f.readlines()]
    return rotations

def solve():
    rotations = get_input()
    curr_position = 50
    password = 0
    for rotation in rotations:
        direction = rotation[0]
        delta = int(rotation[1:])
        if direction == 'L':
            curr_position = (curr_position - delta) % 100
        elif direction == 'R':
            curr_position = (curr_position + delta) % 100
        if curr_position == 0:
            password += 1
    return password
        
def solve2():
    rotations = get_input()
    pos = 50
    password = 0

    for r in rotations:
        direction = r[0]
        delta = int(r[1:])

        if direction == "R":
            # first time hit 0
            first = (100 - pos) % 100
            if first < delta:
                password += 1  # hit the first 0
                # extra hits every 100 steps
                password += (delta - first - 1) // 100

            pos = (pos + delta) % 100

        else:  # L
            first = pos % 100
            if first < delta:
                password += 1
                password += (delta - first - 1) // 100

            pos = (pos - delta) % 100

    return password
        
        
    
    
print(f"Part 1: {solve()}")
print(f"Part 2: {solve2()}")