import os
import requests
import shutil

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

file = open(day_path + "/input.txt", "w")
file.write("\n".join(filter(lambda x: x != "", response.text.split("\n"))))
file.close()

# Copy the template file into the new directory. Once for each part.
print("Copying template python structure...")
shutil.copyfile("part_template.py", day_path + "/part_1.py")
shutil.copyfile("part_template.py", day_path + "/part_2.py")

print("Done!")