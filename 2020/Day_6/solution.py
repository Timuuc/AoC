doc = open('Day_6/input.txt', 'r')
content = doc.readlines()
LENGTH = len(content)
doc.close()

anz = set()
score:int = 0
new_group = True

for ii in range(0, LENGTH):
    line = content[ii]
    if ii < LENGTH - 1: 
        line = line[:-1]
    else:
        anz = set(line) & anz
        score += len(anz)
        new_group = True
        continue

    if line == '':
        score += len(anz)
        new_group = True
        anz = set()
        continue

    if len(anz) == 0 and new_group:
        new_group = False
        anz = set(line)
    else:
        anz = set(line) & anz


print("Winning score is: " + str(score))