file = open("sample.txt", "r")

coords = [0, 0]

mapping = {"1":["1", "2", "3"],
           "0":["4", "5", "6"],
          "-1":["7", "8", "9"]}

final_num = ""

for line in file:
    for char in line:
        if char == "U" and coords[1] != 1:
            coords[1] += 1
        elif char =="D" and coords[1] != -1:
            coords[1] -= 1
        elif char == "R" and coords[0] != 1:
            coords[0] += 1
        elif char == "L" and coords[0] != -1:
            coords[0] -= 1

    final_num += (mapping[str(coords[1])][coords[0]])

print(int(final_num))
file.close()