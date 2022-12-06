def find(n: int) -> int:
    for i in range(len(content)):
        if len(set(content[i:i + n])) == n:
            return i + n

with open('input') as f:
    content = f.read()

print('part one:', find(4))
print('part one:', find(14))
