with open('input') as f:
    content = [ list(map(int, line.rstrip('\n').replace('-', ',').split(','))) for line in f ]

print('part one:', sum([ 1 for a, b, x, y in content if a <= x <= y <= b or x <= a <= b <= y ]))
print('part two:', sum([ 1 for a, b, x, y in content if a <= x <= b or x <= a <= y ]))