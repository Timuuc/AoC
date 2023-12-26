doc = open('Day_5/input.txt', 'r')
content = doc.readlines()
doc.close()
score:int = 0
not_int:int = 0

for line in content:
    a:int = 0
    b:int = 0
    c:int = 0
    d:int = 0
    temp_input:str = ""

    for char in line:
        if char == '-':
            if a == 0:
                a = int(temp_input)
                temp_input = ""
                continue
            else:
                c = int(temp_input)
                temp_input = ""
                continue
        elif char == ',':
            b = int(temp_input)
            temp_input = ""
            continue
        elif char == '\n':
            d = int(temp_input)
            temp_input = ""
            continue

        temp_input += char

    if temp_input != "":   
        d = int(temp_input)

    liste = []
    for i in range (a, b+1):
        liste.append(i)
    ab = set(liste)

    liste = []
    for i in range (c, d+1):
        liste.append(i)
    cd = set(liste)

    """if len(ab) > len(cd):
        x = (cd - ab)
        if len(x) == 0:
            score += 1
    else:
        y = ab - cd 
        if len(y) == 0:
            score += 1"""
    
    x = ab.intersection(cd) 
    if len(x) > 0:
        score += 1
    else:
        not_int += 1
        


print("The score is: " + str(score))