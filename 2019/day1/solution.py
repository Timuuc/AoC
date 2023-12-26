file = open("2019/day1/input.txt")
sum = 0
def fuel_calc(module:int) -> int:
    return (module//3)-2

for line in file:
    if line[-1] == '\n':
        num = int(line[:-1])
    else:
        num = int(line)
    
    module_sum = 0
    
    while True:
        tmp = fuel_calc(num)
        if tmp < 6:
            if tmp > 0:
                module_sum += tmp
            break

        else:
            module_sum += tmp
            num = tmp
    sum += module_sum

print(sum)