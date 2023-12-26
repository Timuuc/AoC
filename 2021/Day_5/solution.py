doc = open("Day_5/input.txt", 'r')
content = doc.readlines()
LENGTH = len(content)
doc.close()

score:int = 0
vents = []

for ii in range(0, LENGTH):
    line = content[ii]

    if ii == LENGTH - 1: line += '\n'
    tmp = ""
    x1:int = 0
    x2:int = 0
    y1:int = 0
    y2:int = 0
    vector2:bool = False

    for char in line:
        if char == ' ' or char == '\n' or char == ',':
            if char == ',':
                if vector2: 
                    x2 = int(tmp)
                else: 
                    x1 = int(tmp)
            elif tmp == "->":
                vector2 = True 
            else:
                if vector2: y2 = int(tmp)
                else:       y1 = int(tmp)
            tmp = ""
            continue
        else: tmp += char
        
    vents.append(((x1, y1), (x2, y2)))

c_vents = []
for vent in vents:
    if ( vent[0][0] == vent[1][0] ) or ( vent[0][1] == vent[1][1] ):
        c_vents.append(vent)
len_c_vents = len(c_vents)

interlaps = []
for jj in range(0, len_c_vents - 1):
    v_line1 = c_vents[jj]
    v_list1 = []

    if v_line1[0][0] > v_line1[1][0]: 
        v1_x1 = v_line1[1][0]
        v1_x2 = v_line1[0][0]
    else:                    
        v1_x1 = v_line1[0][0]
        v1_x2 = v_line1[1][0]
    
    if v_line1[0][1] > v_line1[1][1]: 
        v1_y1 = v_line1[1][1]
        v1_y2 = v_line1[0][1]
    else:                    
        v1_y1 = v_line1[0][1]
        v1_y2 = v_line1[1][1]


    for x in range(v1_x1, v1_x2 + 1):
            for y in range(v1_y1, v1_y2 + 1):
                v_list1.append((x, y))
    v_set1 = set(v_list1)

    for ll in range(jj + 1, len_c_vents - jj):
        v_line2 = c_vents[jj + ll]
        v_list2 = []
       
        if v_line2[0][0] > v_line2[1][0]: 
            v2_x1 = v_line2[1][0]
            v2_x2 = v_line2[0][0]
        else:                    
            v2_x1 = v_line2[0][0]
            v2_x2 = v_line2[1][0]
    
        if v_line2[0][1] > v_line2[1][1]: 
            v2_y1 = v_line2[1][1]
            v2_y2 = v_line2[0][1]
        else:                    
            v2_y1 = v_line2[0][1]
            v2_y2 = v_line2[1][1]

        for x in range(v2_x1, v2_x2 + 1):
            for y in range(v2_y1, v2_y2 + 1):
                v_list2.append((x, y))
        v_set2 = set(v_list2)

        v_set_intl = v_set1 & v_set2

        for e in v_set_intl:
            interlaps.append(e)

intersects = set(interlaps)
print("Winning score is: " + str(len(intersects)))   

