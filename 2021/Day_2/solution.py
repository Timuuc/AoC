doc = open("input.txt", 'r')
content = doc.readlines()
x = int(0)
y = int(0)
aim = int(0)
for line in content:
    cmd = ''
    index = 0
    steps = 0
    for char in line:
        if char == ' ': break
        cmd += char
        index += 1
    steps = line[index + 1]
    if str(cmd) == "forward":
        x += int(steps)
        y += int(steps) * aim
    elif str(cmd) == "up": aim -= int(steps)   
    elif str(cmd) == "down": aim += int(steps)
ans = x * y
print("X: " + str(x) + "  Y: " + str(y) )
print("Answer:" + str(ans))
doc.close()