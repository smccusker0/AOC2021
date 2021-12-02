steps = []
with open('prod.txt') as course:
    for direction in course:
        steps.append(direction.strip().split(" "))

horizontal = 0
depth = 0
aim = 0

for step in steps:
    if step[0] == "forward":
        horizontal += int(step[1])
        depth += aim * int(step[1])
    elif step[0] == "down":
        aim += int(step[1])
    elif step[0] == "up":
        aim -= int(step[1])

print(horizontal * depth)