doc = open('Day_4/input.txt', 'r')
content = doc.readlines()
doc.close()

KEY_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
HCL_HEX = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
ECL_EYE = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

score:int = 0
temp_input:str = ""
temp_pp = []

for line in content:
    if line == "\n":
        temp_pp_s = set(temp_pp)
        m_keys = KEY_FIELDS - temp_pp_s
        if len(m_keys) == 0:
            score += 1
        temp_pp = []
        continue

    for char in line:
        if char == ':':
            cmd = temp_input
            temp_input = ""
            continue
        elif (char == ' ') or (char == '\n'):
            if cmd == "byr":
                if len(temp_input) == 4:
                    year = int(temp_input)

                    if (year >= 1920) and (year <= 2002):
                        temp_pp.append("byr")
            
            elif cmd == "iyr":
                if len(temp_input) == 4:
                    year = int(temp_input)

                    if (year >= 2010) and (year <= 2020):
                        temp_pp.append("iyr")

            elif cmd == "eyr":
                if len(temp_input) == 4:
                    year = int(temp_input)

                    if (year >= 2020) and (year <= 2030):
                        temp_pp.append("eyr")

            elif cmd == "hgt":
                if temp_input[-2:] == "cm":
                    height = int(temp_input[:-2])
                    if (height >= 150) and (height <= 193):
                        temp_pp.append("hgt")
                elif temp_input[-2:] == "in":
                    height = int(temp_input[:-2])
                    if (height >= 59) and (height <= 76):
                        temp_pp.append("hgt")

            elif cmd == "hcl":
                if temp_input[0] == "#" and len(temp_input) == 7:
                    colorcode = set(temp_input[1:])
                    wrong_char = colorcode - HCL_HEX
                    if len(wrong_char) == 0:
                        temp_pp.append("hcl")
            
            elif cmd == "ecl":
                eye_cl = set()
                eye_cl.add(temp_input)
                intrsct = eye_cl.intersection(ECL_EYE)
                if len(intrsct) > 0:
                    temp_pp.append("ecl")

            elif cmd == "pid":
                if len(temp_input) == 9:
                    temp_pp.append("pid")

            temp_input = ""
            continue

        temp_input += char

temp_pp_s = set(temp_pp)
m_keys = KEY_FIELDS - temp_pp_s
if len(m_keys) == 0:
    score += 1
temp_pp = []



print("The score is: " + str(score))
