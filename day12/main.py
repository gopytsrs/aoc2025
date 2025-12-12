def parse(file_path="data.in"):
    regions = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if 'x' in line and ':' in line:
                size_part, counts_part = line.split(':', 1)
                width, height = map(int, size_part.split('x'))
                required_pieces = sum(map(int, counts_part.split()))
                regions.append((width, height, required_pieces))
    return regions


def solve1():
    regions = parse()
    can_fit = 0
    piece_width, piece_height = 3, 3

    for width, height, required_pieces in regions:
        max_pieces_can_fit = (width // piece_width) * (height // piece_height)
        if required_pieces <= max_pieces_can_fit:
            can_fit += 1

    return can_fit

print(f"Part 1: {solve1()}")