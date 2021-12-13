def parse_input():
    with open("../../input/day_13.txt", "r") as file:
        data = [x.split("\n") for x in file.read().split("\n\n")]
        return [[int(i.split(",")[0]), int(i.split(",")[1])] for i in data[0]], [[i.split(" ")[2].split("=")[0], int(i.split(" ")[2].split("=")[1])]for i in data[1]]

paper, instructions = parse_input()
instruction = instructions[0]
if instruction[0] == 'y':
    for i in range(len(paper)):
        if paper[i][1] > instruction[1]:
            paper[i] = [paper[i][0], instruction[1] - (paper[i][1] - instruction[1])]
else:
    for i in range(len(paper)):
        if paper[i][0] > instruction[1]:
            paper[i] = [instruction[1] - (paper[i][0] - instruction[1]), paper[i][1]]

print(len(set([tuple(x) for x in paper])))