def parse_input():
    with open("../../input/day_9.txt", "r") as file:
        return [[int(j) for j in x] for x in [list(i.strip()) for i in file.readlines()]]

def check_neighbours(heightmap, y, x):
    if (y, x) in points_checked:
        return 0

    points_checked.add((y, x))
    neighbours = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    points_to_check = []
    for point in neighbours:
        if point[0] != -1 and point[0] != len(heightmap) and point[1] != -1 and point[1] != len(heightmap[0]):
            if heightmap[point[0]][point[1]] != 9:
                points_to_check.append(point)

    size = 1
    if len(points_to_check) != 0:
        for i in points_to_check:
            size += check_neighbours(heightmap, i[0], i[1])
    return size

heightmap = parse_input()
low_points = set()
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        self = heightmap[y][x]
        top = 10 if y == 0 else heightmap[y - 1][x]
        bottom = 10 if y == len(heightmap) - 1 else heightmap[y + 1][x]
        left = 10 if x == 0 else heightmap[y][x - 1]
        right = 10 if x == len(heightmap[0]) - 1 else heightmap[y][x + 1]
        if top > self and right > self and bottom > self and left > self:
            low_points.add((y, x))

result = []
points_checked = set()
for low_point in low_points:
    result.append(check_neighbours(heightmap, low_point[0], low_point[1]))
result.sort()
print(result[-1]*result[-2]*result[-3])