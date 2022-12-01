with open('input') as f:
    content = f.read()

elves    = [ elves.split('\n') for elves in content.split('\n\n') ]
calories = [ sum(list(map(int, elf))) for elf in elves ]
calories.sort(reverse=True)

print('part one:', calories[0])
print('part two:', sum(calories[:3]))
