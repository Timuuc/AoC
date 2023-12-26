class table:
    def __init__(self, data, ID:int) -> None:
        self.tableDat = data
        self.id:int = ID
        self.bingo = False
    
    def checkBingo(self) -> bool:
        if self.bingo: return False

        #check rows
        for row in self.tableDat:
            tBingo = True
            for pair in row:
                if pair[1] == False:
                    tBingo = False
                    break

            if tBingo:
                self.bingo =tBingo
                return tBingo        
        
        #check coloums
        for ii in range(0, 5):
            tBingo = True
            for jj in range(0, 5):
                if self.tableDat[jj][ii][1] == False:
                    tBingo = False
                    break
            if tBingo:
                self.bingo =tBingo
                return tBingo        
        return False

    def new_num(self, num:int) -> bool:
        for row in range(0, 5):
            for col in range(0, 5):
                if self.tableDat[row][col][0] == num:
                    self.tableDat[row][col] = (int(num), True)
                    return True
        return False
    
    def getScore(self) -> int:
        score:int = 0
        for row in self.tableDat:
            for col in row:
                if not col[1]:  score += col[0]
        
        return score
    
    def getId(self) -> int:
        return self.id
    
    def reset(self) -> None:
        self.bingo = False
        for row in range(0, 5):
            for col in range(0, 5):
                self.tableDat[row][col] = (self.tableDat[row][col][0], False)
            

doc = open("Day_4/input.txt", 'r')

nr_pool = doc.readline()
pool = []

tmp = ""
for ch in nr_pool:
    if ch == ',' or ch == '\n':
        pool.append(int(tmp))
        tmp = ""
        continue
    tmp += ch

doc.readline()

content = doc.readlines()

matrix_index = 0
line_index:int = 0

max_m = (len(content) - 1 ) // 6

table_l = []

for mat in range(0, max_m):
    matrix = []
    for row in range(0, 5):
        row_l = []
        y = (mat * 6) + row

        for col in range(0, 5):
            tmpi:int = 0
            tmpstr:str = ""
            x = col * 3

            for c in range (0, 2):
                if (content[y][x+c] != ' '): tmpstr += content[y][x+c]
            tmpi = int(tmpstr) 
            row_l.append((tmpi, False))
        matrix.append(row_l)
    table_l.append(table(data=matrix, ID=mat + 1))

bingo:bool = False
hit:bool = False
for num in pool:

    for tab in table_l:
        hit = tab.new_num(num)
        if hit:
            bingo = tab.checkBingo()
            if bingo:
                tabId = tab.getId()

winning_tab = table_l[tabId - 1]
winning_tab.reset()

score:int = 0
for num in pool:
    if winning_tab.new_num(num):
        if winning_tab.checkBingo():
            score = winning_tab.getScore() * num
            break

print("Winning score is: " + str(score))   

