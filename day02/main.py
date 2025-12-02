def parse():
    with open("data.in") as f:
        ranges = [tuple(map(int, l.split('-'))) for l in f.read().strip().split(",")]
        print(ranges)
        return ranges


def solve1():
    ranges = parse()
    password = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            string = str(num)
            if len(string) % 2 != 0:
                continue
            mid = len(string) // 2
            if string[:mid] == string[mid:]:
                password += num
    return password

def solve2():
    ranges = parse()
    password = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            string = str(num)
            str_len = len(string)
            for pattern_len in range(1, str_len // 2 + 1):
                if str_len % pattern_len == 0:
                    pattern = string[:pattern_len]
                    if pattern * (str_len // pattern_len) == string:
                        password += num
                        break
    return password
                
            

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
