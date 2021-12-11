def parse_input():
    with open("../../input/day_11.txt", "r") as file:
        return [[int(letter) for letter in line.strip("\n")] for line in file.readlines()]

def increment_all(population):
    return [[i+1 for i in line] for line in population]

def increase_neighbours(population, y, x):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_y = y + i
            new_x = x + j
            if 0 <= new_y < len(population) and 0 <= new_x < len(population[0]):
                if population[new_y][new_x] != -1:
                    population[new_y][new_x] += 1
    return population

population = parse_input()
steps = 0
while True:
    population = increment_all(population)
    something_changed = True
    flashes_in_step = 0
    while something_changed:
        something_changed = False
        for y in range(len(population)):
            for x in range(len(population[0])):
                if population[y][x] > 9:
                    something_changed = True
                    population = increase_neighbours(population, y, x)
                    population[y][x] = -1
                    flashes_in_step += 1
    population = [[i if i != -1 else 0 for i in line] for line in population]
    steps += 1
    if flashes_in_step == len(population)*len(population[0]):
        break

print(steps)