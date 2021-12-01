import os
import requests

# Create directory for the new day
input_day = input("No. day --> ")
day_path = "./day_" + input_day
print("Creating directory " + day_path + "...")
os.mkdir(day_path)

# Read 'session' cookie from file
with open("AoC_session.txt", "r") as file:
    aoc_session = file.readline()

# Pull puzzle input from https://adventofcode.com and parse it into a 'input.txt' file
http_path = "https://adventofcode.com/2021/day/" + input_day + "/input"
print("Pulling input from: " + http_path + "...")
cookies = {"session": aoc_session}
response = requests.get(http_path, cookies=cookies)

file = open("../input" + day_path[1:] + ".txt", "w")
file.write("\n".join(filter(lambda x: x != "", response.text.split("\n"))))
file.close()

print("Copying template files...")
# Copy template files into new day directory
with open("part_template.py", "r") as file:
    template = "".join(file.readlines()).split("{}")

template[0] += input_day
file = open(day_path + "/part_1.py", "w")
file.write("".join(template))
file.close()

file = open(day_path + "/part_2.py", "w")
file.write("".join(template))
file.close()

print("Done!")