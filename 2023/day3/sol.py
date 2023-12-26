with open('day3/input.txt', 'r') as file:
    FILE = file.readlines()
    num_lines = len(FILE)
X = 1
Y = 0

numbers = "0123456789"

def sol1() -> int:
    valid_num = []
    invalid_num = []
    sol = 0
    for y in range(0, num_lines):
        ignore_next = 0
        for x in range(len(FILE[y]) -1):
            if ignore_next > 0:
                ignore_next -= 1
                continue

            cur_chr = FILE[y][x] 

            if cur_chr in numbers:
                num_valid = False
                num_start = [y, x]

                i = x
                while(FILE[y][i] in numbers):
                    i += 1

                num_end = [y, i]
                num_str = FILE[y][num_start[X]:num_end[X]]
                ignore_next = num_end[X] - num_start[X] -1

                number = int(num_str)

                # check for symbols nearby
                if y == 0:
                    check_y_start = 0
                    check_y_end = y +1

                elif y == num_lines -1:
                    check_y_start = y -1
                    check_y_end = y

                else:
                    check_y_start = y -1
                    check_y_end = y +1

                if num_start[X] == 0:
                    check_x_start = num_start[X]
                    check_x_end   = num_end[X] + 1

                elif num_end[X] == len(FILE[num_start[Y]]) -1:
                    check_x_start = num_start[X] -1
                    check_x_end = num_end[X] 

                else:
                    check_x_start = num_start[X] -1
                    check_x_end = num_end[X] +1

                for check_y in range(check_y_start, check_y_end +1):
                    for check_x in range(check_x_start, check_x_end):
                        check_chr = FILE[check_y][check_x]
                        if not (check_chr in numbers) and \
                            check_chr != '.':
                            num_valid = True

                if num_valid:
                    valid_num.append(number)
                else:
                    invalid_num.append(number)

    for num in valid_num:
        sol += num
    
    return sol

def sol2() -> int:
    valid_num = []
    invalid_num = []
    sol2 = 0
    for y in range(0, num_lines):
        for x in range(len(FILE[y]) -1):

            cur_chr = FILE[y][x] 

            if cur_chr == '*':
                gear_valid = False
                num_around_gear = []
                gear_pos = [y, x]

                # check for symbols nearby
                if gear_pos[Y] == 0:
                    check_y_start = 0
                    check_y_end = gear_pos[Y] +1

                elif gear_pos[Y] == num_lines -1:
                    check_y_start = gear_pos[Y] -1
                    check_y_end = gear_pos[Y]

                else:
                    check_y_start = gear_pos[Y] -1
                    check_y_end = gear_pos[Y] +1

                if gear_pos[X] == 0:
                    check_x_start = gear_pos[X]
                    check_x_end   =gear_pos[X] + 1

                elif gear_pos[X] == len(FILE[gear_pos[Y]]) -1:
                    check_x_start = gear_pos[X] -1
                    check_x_end = gear_pos[X] 

                else:
                    check_x_start = gear_pos[X] -1
                    check_x_end = gear_pos[X] +1
                
                
                for check_y in range(check_y_start, check_y_end +1):
                    ignore_next = 0
                    for check_x in range(check_x_start, check_x_end +1):

                        if ignore_next > 0:
                            ignore_next -= 1
                            continue

                        check_chr = FILE[check_y][check_x]
                        if check_chr in numbers:
                            i = check_x
                            while(FILE[check_y][i] in numbers):
                                i += 1
                            num_end = i

                            j = check_x
                            while(FILE[check_y][j] in numbers):
                                j -= 1
                            num_start = j +1

                            num_str = FILE[check_y][num_start:num_end] 
                            num = int(num_str)
                            num_around_gear.append(num)
                            ignore_next = num_end - check_x -1
                
                if len(num_around_gear) == 2:
                    sol2 += num_around_gear[0] * num_around_gear[1]

    return sol2

solution1 = sol1()
print (f'Part numbers: {solution1}')
solution2 = sol2()
print (f'Gear numbers: {solution2}')
    