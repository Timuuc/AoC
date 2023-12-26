file = open("2023/day4/input.txt")

line_number = 1
total_score = 0

for line in file:
    if len(line) == 0:
        break
    drawn_numbers = set()
    winning_numbers = set()

    drawn_numbers_str = line[10:39]
    if line[-1] == "\n":
        win_numbers_str = line[42:-1]
    else:
        win_numbers_str = line[42:]

    buffer = ""
    for chr in drawn_numbers_str:
        if chr == " " and len(buffer) != 0:
            drawn_numbers.add(int(buffer))
            buffer = ""
        if chr != " ":
            buffer += chr
    drawn_numbers.add(int(buffer))

    buffer = ""
    for chr in win_numbers_str:
        if (chr == " " or chr == "\n") and len(buffer) != 0:
            winning_numbers.add(int(buffer))
            buffer = ""
        if chr != " ":    
            buffer += chr
    winning_numbers.add(int(buffer))

    set_matches = winning_numbers.intersection(drawn_numbers)

    matches = len(set_matches)

    score = 0
    if matches != 0:
        score = 2 ** (matches -1)
    total_score += score

    print (f'Card {line_number} score: {score}')
    line_number += 1

print(f'total score: {total_score}')