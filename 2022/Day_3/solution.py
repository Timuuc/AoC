def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:half*2]

doc = open('Day_3/input.txt', 'r')
content = doc.readlines()
doc.close()

lookup_map = [('a',1),('b',2),('c',3),('d',4),('e',5),('f',6), \
              ('g',7),('h',8),('i',9),('j',10),('k',11),('l',12),('m',13), \
              ('n',14),('o',15),('p',16),('q',17),('r',18),('s',19),('t',20), \
              ('u',21),('v',22),('w',23),('x',24),('y',25),('z',26),('A',27), \
              ('B',28),('C',29),('D',30),('E',31),('F',32),('G',33),('H',34), \
              ('I',35),('J',36),('K',37),('L',38),('M',39),('N',40),('O',41), \
              ('P',42),('Q',43),('R',44),('S',45),('T',46),('U',47),('V',48), \
              ('W',49),('X',50),('Y',51),('Z',52)]

# Solution part one
score:int = 0
for line in content:
    bag1, bag2 = split_list(line)
    bag1 = set(bag1)
    bag2 = set(bag2)
    char1 = bag1 & bag2
    for char in char1:
        for pair in lookup_map:
            if pair[0] == char:
                score += pair[1]          
print("The score is: " + str(score))

# Solution Part two
score:int = 0                 
for i in range(0, 300, 3):
    elf1 = set(content[i]) - {'\n'}
    elf2 = set(content[i+1]) - {'\n'}
    elf3 = set(content[i+2]) - {'\n'}
    item = elf1 & elf2 & elf3
    for e in item:
        for pair in lookup_map:
            if e == pair[0]:
                score += pair[1]
print("The score is: " + str(score))