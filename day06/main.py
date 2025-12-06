from functools import reduce
from operator import mul, add
from collections import defaultdict

def parse1():
    with open("data.in", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    operands = [list(map(int, line.split())) for line in lines[:-1]]
    operators = lines[-1].split()
    return operands, operators

def solve1():
    operands, operators = parse1()
    total = 0
    for i in range(len(operators)):
        operator = operators[i]
        values = [row[i] for row in operands]
        if operator == '+':
            result = reduce(add, values, 0)
        elif operator == '*':
            result = reduce(mul, values, 1)
        total += result
    return total

def parse2():
    with open('data.in', 'r') as f:
        lines = [line[:-1] for line in f.readlines()]
    operators = lines[-1].split()
    groups = defaultdict(lambda:defaultdict(int))
    
    for line in lines[:-1]:
        line = list(line)
        group = 0
        num_seen = False
        for col in range(len(line)):
            if line[col] == ' ':
                if num_seen:
                    group += 1
                    num_seen = False
                else:
                    continue
            else:
                num_seen = True
                groups[group][col] *= 10
                groups[group][col] += int(line[col])
    return operators, groups

def solve2():
    operators, groups = parse2()
    result = 0
    for group, operator in enumerate(operators):
        values = list(groups[group].values())
        if operator == '+':
            result += reduce(add, values, 0)
        elif operator == '*':
            result += reduce(mul, values, 1)
    return result
                
                
                        
print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")
                