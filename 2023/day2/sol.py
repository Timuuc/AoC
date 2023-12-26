config = { "red"   : 12, 
           "green" : 13,
           "blue"  : 14 }

def get_game_id(line:str) -> [int, int]:
    
    chr_id = 0
    id_after_id = 0
    
    for chr_id in range(4, len(line) -1):

        if line[chr_id] == ':':
            id_after_id = chr_id
        
        if id_after_id != 0:
            break
    
    return int(line[5:id_after_id]), id_after_id +2

def get_current_sets(line:str):
    
    buffer = ""
    game = []
    sets = []
    num_set = False
    col_set = False

    for chr in line:
        if chr == ' ' and len(buffer) != 0:
            num = int(buffer)
            num_set = True
            buffer = ""
        elif chr == ',':
            col = buffer
            col_set = True
            buffer = ""

        elif chr == ";" or chr == "\n":
            col = buffer
            sets.append([col, num])
            num_set = False
            col_set = False
            
            game.append(sets)
            sets = []
            buffer = ""
        
        else: 
            if chr != ' ':
                buffer += chr

        if num_set and col_set:
            sets.append([col, num])
            num_set = False
            col_set = False
    
    return game


file = open("day2/input.txt")

sum = 0
sum_2 = 0

for line in file:
    possible = True
    id, set_start = get_game_id(line)

    line = line[set_start:]

    # find if its possible
    current_sets = get_current_sets(line)

    for set in current_sets:
        for draw in set:
            if config[draw[0]] < draw[1]:
                possible = False
                break

    if possible:
        sum += id
    
    # part two
    min_num= { "red"   : 0, 
               "green" : 0,
               "blue"  : 0 }
    
    for set in current_sets:
   
        for draw in set:
            if min_num[draw[0]] < draw[1]:
                min_num[draw[0]] = draw[1]
    
    set_mult = min_num["red"] * min_num["green"] * min_num["blue"]
    print(f'Sum of Sets min {set_mult}')

    sum_2 += set_mult

 
print(f'Sum of IDs is {sum}')
print(f'Sum of mins is {sum_2}')
