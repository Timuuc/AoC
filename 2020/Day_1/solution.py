doc = open('Day_1/input.txt', 'r')
content = doc.readlines()
doc.close()

a:int = 0
b:int = 0
c:int = 0
max:int = len(content)
tf:bool = False

for ii in range(0, max):
    if tf: break
    if ii < (max - 1): line_a = content[ii][:-1]
    else:              line_a = content[ii]

    a = int(line_a)

    for jj in range(ii+1, max):
        if tf: break
        if jj < (max - 1): line_b = content[jj][:-1]
        else:              line_b = content[jj]
    
        b = int(line_b)

        for ll in range (jj+1, max):
            if ll < (max - 1): line_c = content[ll][:-1]
            else:              line_c = content[ll]

            c = int(line_c)
            
            if a + b + c == 2020:
                tf = True
                break


score = a * b * c

print("The score is: " + str(score))
print("Die Zahl a ist " + str(a))
print("Die Zahl b ist " + str(b))
print("Die Zahl c ist " + str(c))