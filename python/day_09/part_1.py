def parse_input():
    with open("../../input/day_9.txt", "r") as file:
        return [[int(j) for j in x] for x in [list(i.strip()) for i in file.readlines()]]

heightmap = parse_input()
result = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        self = heightmap[y][x]
        top = 10 if y == 0 else heightmap[y - 1][x]
        bottom = 10 if y == len(heightmap) - 1 else heightmap[y + 1][x]
        left = 10 if x == 0 else heightmap[y][x - 1]
        right = 10 if x == len(heightmap[0]) - 1 else heightmap[y][x + 1]
        if top > self and right > self and bottom > self and left > self:
            result += self + 1

print(result)