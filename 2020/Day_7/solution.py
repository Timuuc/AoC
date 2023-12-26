doc = open('Day_7/test.txt', 'r')
content = doc.readlines()
LENGTH = len(content)
doc.close()
score:int = 0
update:bool = True

g_bags = ["shinygold"]
v_bags = []

for ii in range(0, LENGTH):
    line = content[ii]
    if ii == LENGTH - 1:
         line += '\n'
    tmp_str = ""
    adj = ""
    clr = ""
    main_bag = ""
    bags = []
    cont_act = False
    cont_nr_bag_av = False
    for char in line:
        if char == ' ' or char == '\n':
            if not cont_act:
                if adj == "":   adj = tmp_str
                elif clr == "": clr = tmp_str
                else:
                    main_bag = adj + clr
                    clr = ""
                    adj = ""
                    cont_act = True
            else:
                if tmp_str == "contain": cont_nr_bag_av = True
                elif cont_nr_bag_av: cont_nr_bag_av = False
                elif adj == "": adj = tmp_str
                elif clr == "": clr = tmp_str
                elif tmp_str[-1:] == ',' or tmp_str[-1:] == '.':
                    bags.append(adj + clr)
                    clr = ""
                    adj = ""
                    cont_nr_bag_av = True
                    if tmp_str == '.':
                        break             
            tmp_str = ""
            continue
        tmp_str += char
    
    v_bags.append((main_bag, bags))

update = True
while update:
    update = False

    for v_bag in v_bags:
        ignore = False            
        for g_bag in g_bags:
            if v_bag[0] == g_bag:
                ignore = True
                break
        if ignore: break

        for v_c_bag in v_bag[1]:
            if update: break
            for g_bag in g_bags:
                if v_c_bag == g_bag:
                    g_bags.append(v_bag[0])
                    update = True
                    break
    


                       

                    

score = len(g_bags) - 1

print("Winning score is: " + str(score))