import copy

with open('input') as f:
    content = f.readlines()

cranes = {
    1: ['S', 'T', 'H', 'F', 'W', 'R'],
    2: ['S', 'G', 'D', 'Q', 'W'],
    3: ['B', 'T', 'W'],
    4: ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
    5: ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
    6: ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
    7: ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
    8: ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
    9: ['L', 'G', 'B', 'W'],
}
commands = [ list(map(int,command.rstrip('\n').split(' ')[1::2])) for command in content[10:] ]

cargos = copy.deepcopy(cranes)
for many, of, to in commands:
    cargos[to] += cargos[of][-many:][::-1]
    cargos[of]  = cargos[of][:-many]
print('part one:', ''.join(f'{value[-1]}' for key, value in cargos.items()))

cargos = copy.deepcopy(cranes)
for many, of, to in commands:
    cargos[to] += cargos[of][-many:]
    cargos[of]  = cargos[of][:-many]
print('part two:', ''.join(f'{value[-1]}' for key, value in cargos.items()))
