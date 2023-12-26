class dir_c:
    typ = "dir"
    d_parent = ""
    d_name  = ""
    content = []
    size:int = 0

    def __init__(self, name:str, parent:str) -> None:
        self.d_name = name
    
    def add(self, new_dir ) -> None:
        self.content.append(new_dir)

    def getSize(self) -> int:
        for obj in self.content:
            self.size += obj.getSize()

        return self.size

class file_c:
    typ = "fil"
    parent:dir_c
    f_name = ""
    size:int = 0

    def __init__(self, name:str, parent:dir_c, size:int) -> None:
        self.f_name = name
        self.d_parent = parent
        self.size = size
    
    def getSize(self) -> int:
        return self.size

doc = open('Day_7/input.txt', 'r')
content = doc.readlines()
doc.close()
score:int = 0

content_true = False
av_dirs = ['/']
layer = 0
myPC = dir_c(name="$", parent="")
root = dir_c(name="/", parent=myPC)
myPC.add(root)
activDir = myPC

for line in content:
    
    tmp = ""
    cmd = ""
    cmd_true = False
    new_dir = False
    new_data = False

    for char in line:
        if char == ' ' or char == '\n':
            if tmp == "$": 
                cmd_true = True
                content_true = False
        
            elif cmd_true:
                cmd = tmp
                cmd_true = False
            
            elif content_true:
                if new_dir:
                    tmpDir = dir_c(name=tmp, parent=activDir)
                    activDir.add(tmpDir)
                    new_dir = False
                
                elif new_data:
                    activDir.add(file_c(name=tmp, parent=activDir))
                    new_data = False

                elif tmp == "dir": new_dir = True
                
                else:
                    score += int(tmp)    
                    new_data = True

            elif cmd == "cd":
                cmd = ""
                if tmp == "..":
                    activDir = activDir.d_parent
                else:
                    for dir in activDir.content:
                        if dir.d_name == tmp:
                            activDir = dir
                            break
            
            if cmd == "ls":
                cmd = ""
                content_true = True
                break
                            
            tmp = ""
            continue

        tmp += char

 

print("The score is: " + str(score))