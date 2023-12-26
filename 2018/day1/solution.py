sum = 0

PartSum = []
Seen_PartSum = set()

while True:
    file = open("2018/day1/input.txt")
    for line in file:
        if line[-1] == '\n':
            symbol = line[0]
            num = int(line[1:-1])
        else:
            symbol = line[0]
            num = int(line[1:])
        
    
        if symbol == '+':
            sum += num
        else:
            sum -= num


        if sum in Seen_PartSum:
            print(sum)
            break

        Seen_PartSum.add(sum)
    else:
        continue
    break

