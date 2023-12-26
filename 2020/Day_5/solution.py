doc = open('Day_5/input.txt', 'r')
content = doc.readlines()
doc.close()

temp_input:str = ""
liste = []
row:int
column:int

max_line:int = 0
passes = []

for line in content:
    min:int = 0
    max:int = 127
    minc:int = 0
    maxc:int = 7
    row_new:int = 0
    column_new:int = 0
    ID:int = 0

    for char in line:
        if char == 'F':
            max = min + ((max - min) // 2)
            continue
        elif char == 'B':
            min = min + (((max - min) + 1) // 2)
        elif char == 'L':
            maxc = minc + ((maxc - minc) // 2)
        elif char == 'R':
            minc = minc + (((maxc - minc) + 1) // 2)
    
    line_sum:int = max * 8 + maxc
    passes.append(line_sum)
    
    if max_line < line_sum: max_line = line_sum
    """"
    row = []
    column = []   

    for char in line:       
        if char == 'F':
            row_new = len(row) // 2
            max_new = max - row_new
            max = max_new
        elif char == 'B':
            row_new = len(row) // 2
            min_new = row_new - min 
            min = min_new
        elif char == 'L':
            column_new = len(column) // 2
            maxc_new = maxc - column_new
            maxc = max_new
        elif char == 'R':
            column_new = len(column) // 2
            minc_new = column_new - minc
            minc = minc_new

        for max in range(min, max):
            row.append(max)

        for maxc in range(minc, maxc):
            column.append(maxc)
   

    ID = row * 8 + column
    liste.append(ID)
    
    
max_ID = None

for num in liste:
    if(max_ID is None or num > max_ID):
        max_ID = num
"""

passes.sort()
lookup = []

for i in range (passes[0],passes[len(passes) - 1]):
    lookup.append(int(i))

lookup = set(lookup)
passes = set(passes)

ticket = lookup - passes

ticketId = ticket.pop()

print("The score is: " + str(ticketId))
