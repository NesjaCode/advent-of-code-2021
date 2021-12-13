def parse_input():
    with open("../../input/day_13.txt", "r") as file:
        data = [x.split("\n") for x in file.read().split("\n\n")]
        return [[int(i.split(",")[0]), int(i.split(",")[1])] for i in data[0]], [[i.split(" ")[2].split("=")[0], int(i.split(" ")[2].split("=")[1])]for i in data[1]]

paper, instructions = parse_input()
for instruction in instructions:
    if instruction[0] == 'y':
        for i in range(len(paper)):
            if paper[i][1] > instruction[1]:
                paper[i] = [paper[i][0], instruction[1] - (paper[i][1] - instruction[1])]
    else:
        for i in range(len(paper)):
            if paper[i][0] > instruction[1]:
                paper[i] = [instruction[1] - (paper[i][0] - instruction[1]), paper[i][1]]

paper = set([tuple(x) for x in paper])
visual = [[" " for i in range(max(map(lambda x: x[0], paper)) + 1)] for j in range(max(map(lambda x: x[1], paper)) + 1)]
for point in paper:
    visual[point[1]][point[0]] = "#"

for line in visual:
    print("".join(line))