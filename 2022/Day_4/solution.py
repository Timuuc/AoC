doc = open('Day_5/input.txt', 'r')
content = doc.readlines()
doc.close()
score:int = 0
not_int:int = 0
lgth = len(content)

trunk_ld = False
line_ld = False
container_line:int = 0


for ii in range(0, lgth):
    if line_ld: break
    line = content[ii]
    for char in line:
        if char == '1':
            container_line = ii
            line_ld = True
            break
    
line = content[container_line]

max_container:int = 0
container = []
container_index = []

for jj in range(len(line)):
    char = line[jj]

    if char == ' ': continue
    elif char == '\n': break

    container_index.append(int(jj))
    max_container += 1
    
for i in range(0, max_container):
    x = container_index[i]
    container_str = ""
    for y in range(0, container_line , 1):
        char = content[y][x]

        if char != ' ':
            container_str += char
        
    container.append(container_str)
    
cmds = False
doc_end = False

for ii in range(0, len(content)):
    if ii < len(content): line = content[ii]
    if ii == len(content) - 1: line += '\n'



    if line == "\n": 
        cmds = True
        continue
        
    if cmds:
        tmp_str:str = ""
        cont1Id:int = 0
        cont2Id:int = 0
        steps:int = 0
        stps_av = False
        Id1_av  = False
        Id2_av  = False
        av_ch   = False
        up_ch   = False
        load:chr = ''
        
        for char in line:
            if char == ' ' or char == '\n':
                if tmp_str == "move":
                    stps_av = True
                    av_ch = True
                elif tmp_str == "from":
                    Id1_av = True
                    av_ch = True
                elif tmp_str == "to":
                    Id2_av = True
                    av_ch = True
                    
                if av_ch:
                    tmp_str = ""
                    av_ch = False
                    continue
                      
                if Id1_av:
                    cont1Id = int(tmp_str) - 1
                    Id1_av = False
                    up_ch = True
                elif Id2_av:
                    cont2Id = int(tmp_str) - 1
                    Id2_av = False
                    up_ch = True
                elif stps_av:
                    steps = int(tmp_str)
                    stps_av = False
                    up_ch = True   
                    
                if up_ch:
                    tmp_str = ""
                    up_ch = False
                    continue
            tmp_str += char
            
        cmd_rdy = True     
        tmp = container[cont1Id][:steps]
        container[cont1Id] = container[cont1Id][steps:]
        container[cont2Id] = tmp + container[cont2Id]
                        

    
end_str = ""

for i in range(0, max_container):
    if len(container[i]) > 0:
        end_str += container[i][0]
    else: end_str += '.'
        


print("The score is: " + end_str)