doc = open('Day_3/input.txt', 'r')
content = doc.readlines()
doc.close()

X = 0
Y = 1
total:int = 1


for i in range(0,5):
    
    doc_end = False
    if   i == 0: SLOPE = [1,1]
    elif i == 1: SLOPE = [3,1]
    elif i == 2: SLOPE = [5,1]
    elif i == 3: SLOPE = [7,1]
    else:        SLOPE = [1,2]

    score:int = 0
    pos = [int(0), int(0)]

    for ii in range (0, len(content)):

        if ii < len(content) -1:
            line = content[pos[Y]][:-1]
        else:
            line = content[pos[Y]]
        maxz = len(line)
    
        if line[pos[X]] == '#':
            score += 1

        if doc_end: break
    
        pos[X] += SLOPE[X]
        if pos[X] >= maxz:
            pos[X] = pos[X] % maxz
        pos[Y] += SLOPE[Y] 
        if pos[Y] >= len(content):
            pos[Y] = len(content) - 1
            doc_end = True
   
    total *= score


print("The score is: " + str(total))
