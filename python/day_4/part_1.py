def parse_input():
    with open("../../input/day_4.txt", "r") as file:
        input_data = file.read().split("\n\n")
        return [int(x) for x in input_data[0].split(",")], [x.split("\n") for x in input_data[1:]]

def check_winning_condition(boards):
    win = False
    for board in boards:
        for row in board:
            if row.count(-1) == len(row):
                win = True

        if not win:
            for i in range(len(board)):
                column = []
                for j in range(len(board[0])):
                    column.append(board[j][i])

                if column.count(-1) == len(column):
                    win = True

        if win:
            sum_of_unmarked = 0
            for row in board:
                for number in row:
                    if number != -1:
                        sum_of_unmarked += number
            return True, sum_of_unmarked
    return False, 0

numbers, boards = parse_input()
for i in range(len(boards)):
    for j in range(len(boards[0])):
        boards[i][j] = [int(x) for x in boards[i][j].strip().split(" ") if x != ""]

for i in numbers:
    for x in range(len(boards)):
        for y in range(len(boards[0])):
            if i in boards[x][y]:
                boards[x][y][boards[x][y].index(i)] = -1
                win, result = check_winning_condition(boards)
                if win:
                    print(result*i)
                    exit()