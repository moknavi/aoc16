file = open("input.txt", "r")

turn_right = {"N":"E", "E":"S", "S":"W", "W":"N"}
turn_left = {"N":"W", "W":"S", "S":"E", "E":"N"}
facing = "N"
x = 0
y = 0
log = []

for line in file:
    instructions = line.split(",")
    instructions = [i.strip() for i in instructions]


for instr in instructions:
    rotation = instr[0]
    if rotation == "L":
        facing = turn_left[facing]
    elif rotation == "R":
        facing = turn_right[facing]

    value = int(instr[1:len(instr)])

    if facing == "N":
        for i in range(1, value + 1):
            y += 1
            if (x, y) in log:
                print((x, y))
            else:
                log.append((x, y))
    elif facing == "W":
        for i in range(1, value + 1):
            x -= 1
            if (x, y) in log:
                print((x, y))
            else:
                log.append((x, y))
    elif facing == "S":
        for i in range(1, value + 1):
            y -= 1
            if (x, y) in log:
                print((x, y))
            else:
                log.append((x, y))
    elif facing == "E":
        for i in range(1, value + 1):
            x += 1
            if (x, y) in log:
                print((x, y))
            else:
                log.append((x, y))

print(log)
file.close()