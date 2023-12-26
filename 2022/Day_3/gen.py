f= open("Day_3\gen.txt","w+")

f.write("lookup_map = [")

index:int = 1

for i in range(97, 123, 1):
    char = chr(i)
    f.write("('" + char + "'" +  ',' + str(index) + '),')
    index += 1
    if (index % 7 == 0): f.write(", \\\n              ")

for i in range(65, 91, 1):

    char = chr(i)   
    f.write("('" + char + "'" + ',' + str(index) + '),')
    index += 1
    if (index % 7 == 0): f.write(", \\\n              ")

f.write(']')
f.close()