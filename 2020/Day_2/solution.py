doc = open('Day_2/input.txt', 'r')
content = doc.readlines()
doc.close()

score:int = 0

length = len(content)
index = 0

for line in content:
    index += 1
    min:int        = 0
    max:int        = 0
    policy_char:chr       = ''
    tmp_nr_str:str = ""

    for char in line:
        if char == '-':
            min = int(tmp_nr_str) - 1
            tmp_nr_str = ""
            continue
        elif char == ' ':
            if max == 0: max = int(tmp_nr_str) - 1
            tmp_nr_str = ""
            continue
        elif char == ':':
            policy_char = tmp_nr_str[0]
            continue
        tmp_nr_str += char
    
    if index < length: pw:str = tmp_nr_str[:-1]
    else:              pw:str = tmp_nr_str
    anz:int = pw.count(policy_char)

    if (pw[min] == policy_char) ^ (pw[max] == policy_char):
        score += 1


print("The score is: " + str(score))
