doc = open("Day_3_Binary_Diagnostic/input.txt", 'r')
content = doc.readlines()

len = content[0].__len__() - 1

gamma_rate = []
epsilon_rate = []

for index in range(len):

    zeros = int(0)
    ones = int(0)

    for line in content:
        if line[index] == '0': 
            zeros += 1

        else: 
            ones += 1
    
    if zeros > ones:
        gamma_rate.append('0')
        epsilon_rate.append('1')

    else:
        gamma_rate.append('1')
        epsilon_rate.append('0')

gamma_str = ""
epsi_str = ""

for char in gamma_rate:
    gamma_str += char

for char in epsilon_rate:
    epsi_str += char

gamma = int(gamma_str, 2)
epsilon = int(epsi_str, 2)
poCon = epsilon * gamma

print("Gamma   Rate: " + str(gamma))
print("Epsilon Rate: " + str(epsilon))
print("Power Consumption: " + str(poCon)) 
doc.close()

doc = open("Day_3_Binary_Diagnostic/input.txt", 'r')
cont_keep_oxy = doc.readlines()

for index in range(len):

    zeros = int(0)
    ones = int(0)
    cont_ones = []
    cont_zeroes = []

    if cont_keep_oxy.__len__() == 1:
        break

    for line in cont_keep_oxy:
        if line[index] == '0': 
            zeros += 1
            cont_zeroes.append(line)

        else: 
            ones += 1
            cont_ones.append(line)
    
    if zeros > ones:
        cont_keep_oxy = cont_zeroes

    else:
        cont_keep_oxy = cont_ones
        
oxy_str = ""

for char in cont_keep_oxy:
    oxy_str += char

Oxygen_generator_rating = int(oxy_str, 2)
print("Oxygen Generator Rating: " + str(Oxygen_generator_rating))
doc.close()

doc = open("Day_3_Binary_Diagnostic/input.txt", 'r')
cont_keep_co2 = doc.readlines()

for index in range(len):

    zeros = int(0)
    ones = int(0)
    cont_ones = []
    cont_zeroes = []

    if cont_keep_co2.__len__() == 1:
        break

    for line in cont_keep_co2:
        if line[index] == '0': 
            zeros += 1
            cont_zeroes.append(line)

        else: 
            ones += 1
            cont_ones.append(line)
    
    if zeros <= ones:
        cont_keep_co2 = cont_zeroes

    else:
        cont_keep_co2 = cont_ones
        
co2_str = ""

for char in cont_keep_co2:
    co2_str += char

CO2_scrubber_rating = int(co2_str, 2)
print("CO2 scrubber rating: " + str(CO2_scrubber_rating))

life_support = CO2_scrubber_rating * Oxygen_generator_rating
print("Life Support rating: " + str(life_support))
doc.close()