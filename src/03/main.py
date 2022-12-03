priority = lambda x: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(x) + 1

with open('input') as f:
    content = [ line.rstrip('\n') for line in f ]

rucksacks = [ (rucksack[:(len(rucksack) // 2)], rucksack[(len(rucksack) // 2):]) for rucksack in content ]
groups    = [ content[i:i + 3] for i in range(0, len(content), 3) ]

print('part one:', sum([ priority((set(first) & set(second)).pop()) for first, second in rucksacks ]))
print('part two:', sum([ priority((set(first) & set(second) & set(third)).pop()) for first, second, third in groups ]))
