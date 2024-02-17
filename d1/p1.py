file = open("input.txt", "r")

instructions = []
turn_right = {"N":"E", "E":"S", "S":"W", "W":"N"}
turn_left = {"N":"W", "W":"S", "S":"E", "E":"N"}
facing = "N"
north = 0
south = 0
east = 0
west = 0

for line in file:
    instructions = line.split(",")
    instructions = [i.strip() for i in instructions]

for instr in instructions:
    rotation = instr[0]
    print(instr)
    if rotation == "L":
        facing = turn_left[facing]
    elif rotation == "R":
        facing = turn_right[facing]

    value = int(instr[1:len(instr)])

    if facing == "N":
        north += value
    if facing == "W":
        west += value
    if facing == "S":
        south += value
    if facing == "E":
        east += value

horDist = abs(north - south)
verDist = abs(east - west)
    
print(horDist + verDist)
file.close()