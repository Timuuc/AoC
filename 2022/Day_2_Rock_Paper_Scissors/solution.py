doc = open('2022/Day_2_Rock_Paper_Scissors/input.txt', 'r')

content = doc.readlines()

CHAR = 0
VALUE = 1

OP = 0
ME = 2

WIN = ('Z', 6)
DRAW = ('Y', 3)
LOST = ('X', 0)

ROCK_ME = ('X', 1)
PAPER_ME = ('Y', 2)
SCISSORS_ME = ('Z', 3)

ROCK_OP = 'A'
PAPER_OP = 'B'
SCISSORS_OP = 'C'

score:int = 0

for line in content:
    
    if line[ME] == WIN[CHAR]:
        outcome:int = WIN[VALUE]

        if   line[OP] == PAPER_OP[CHAR]:    shape:int = SCISSORS_ME[VALUE]
        elif line[OP] == ROCK_OP[CHAR]:     shape:int = PAPER_ME[VALUE]
        else:                               shape:int = ROCK_ME[VALUE]

    elif line[ME] == DRAW[CHAR]:
        outcome:int = DRAW[VALUE]

        if   line[OP] == PAPER_OP[CHAR]:    shape:int = PAPER_ME[VALUE]
        elif line[OP] == ROCK_OP[CHAR]:     shape:int = ROCK_ME[VALUE]
        else:                               shape:int = SCISSORS_ME[VALUE]

    else: 
        outcome:int = LOST[VALUE]

        if   line[OP] == PAPER_OP[CHAR]:    shape:int = ROCK_ME[VALUE]
        elif line[OP] == ROCK_OP[CHAR]:     shape:int = SCISSORS_ME[VALUE]
        else:                               shape:int = PAPER_ME[VALUE]

    score += (shape + outcome)

print("The total score would be: " + str(score))

doc.close()
