from operator import index


doc = open('input.txt', 'r')

content = doc.readlines()

elf = 1
sum = 0

sum_max = [ 0, 0, 0 ]
elf_max = [ 0, 0, 0 ]

for line in content:
    
    if line != '\n':
        num = int(line)
        #print(str(num))
        sum += num
        continue
    
    print("Elf Nr." + str(elf) + " has " + str(sum) + " Cal.")

    for index in (0, 1, 2):
        if sum_max[index] < sum:
            sum_max[index] = sum
            elf_max[index] = elf
            break

        
    elf += 1
    sum = 0

totalSum = int(sum_max[0]) + int(sum_max[1]) + int(sum_max[2])        

print("Elf " + str(elf_max[0]) + " has " + str(sum_max[0]) + (" Cal.") ) 
print("Elf " + str(elf_max[1]) + " has " + str(sum_max[1]) + (" Cal.") ) 
print("Elf " + str(elf_max[2]) + " has " + str(sum_max[2]) + (" Cal.") )
print("Total: " + str(totalSum) + " Cal." )   
