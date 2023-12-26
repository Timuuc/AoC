doc = open('Day_6/input.txt', 'r')
line = doc.readline()
doc.close()
score:int = 0
code = ""
index:int = 0

for char in line:       
    if len(code) >= 14:
        code_s = set(code)
        if len(code_s) == 14:
            break
        code = code[1:] + char
        index += 1
        continue
    index += 1    
    code += char

print("The score is: " + str(index))