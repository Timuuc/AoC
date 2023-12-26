OK = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

doc = open("input.txt", 'r')

content = doc.readlines()

cur = 0
last = 0
inc = 0

ii = 0
last_block  = 0
nr_lines = content.__len__()
for line in content:

    block = 0

    if (nr_lines <= (ii + 2) ):
        break

    for jj in (0, 1, 2):
        block += int(content[ii + jj])
    
    cur = int(line)
    print("Value: " + str(cur) + " Block: " + str(block), end=" ")

    if (last_block == 0): 
        print(WARNING + "(N/A - no previous measurement)" + ENDC)
    
    elif(last_block == block):
        print(WARNING + "(no change)" + ENDC)

    elif(last_block < block):
        print(OK + "(increased)" + ENDC )
        inc += 1
    else: 
        print(FAIL + "(decreased)" + ENDC )

    last_block = block
    ii += 1

print(OK + str(inc) + ENDC + " were larger than the previous ones.")
print("file has " + str(nr_lines) + " number of lines.")
doc.close()