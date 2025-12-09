from shapely import Polygon
from itertools import combinations

def parse():
    with open("data.in", "r") as f:
        return [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

def solve1():
    positions = parse()
    N = len(positions)
    max_area = 0
    for i1 in range(N):
        for i2 in range(i1 + 1, N):
            y1, x1 = positions[i1]
            y2, x2 = positions[i2]
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            max_area = max(max_area, area)
    return max_area


def solve2():
    positions = parse()

    poly = Polygon([(x, y) for (y, x) in positions])

    max_area = 0

    for (y1, x1), (y2, x2) in combinations(positions, 2):

        xmin, xmax = sorted([x1, x2])
        ymin, ymax = sorted([y1, y2])

        rect = Polygon([
            (xmin, ymin),
            (xmin, ymax),
            (xmax, ymax),
            (xmax, ymin)
        ])

        if poly.contains(rect):
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            max_area = max(max_area, area)

    return max_area

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
            