game_one = {
    ('A', 'X'): 3 + 1, ('A', 'Y'): 6 + 2, ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1, ('B', 'Y'): 3 + 2, ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1, ('C', 'Y'): 0 + 2, ('C', 'Z'): 3 + 3,
}

game_two = {
    ('A', 'X'): 0 + 3, ('A', 'Y'): 3 + 1, ('A', 'Z'): 6 + 2,
    ('B', 'X'): 0 + 1, ('B', 'Y'): 3 + 2, ('B', 'Z'): 6 + 3,
    ('C', 'X'): 0 + 2, ('C', 'Y'): 3 + 3, ('C', 'Z'): 6 + 1,
}

with open('input') as f:
    content = [ line.rstrip('\n').split(' ') for line in f ]

print('part one:', sum([ game_one[(first, second)] for first, second in content ]))
print('part two:', sum([ game_two[(first, second)] for first, second in content ]))
