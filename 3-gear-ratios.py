with open("adventofcode2023/data/3-long.txt", "r") as f:
    input = f.readlines()

def get_symbol_locs(input):
    symbols = {}
    for line_num, line in enumerate(input):
        char_list = list(line.strip())
        for char_num, char in enumerate(char_list):
            if char == "*":
                symbols[(line_num, char_num)] = []
    return symbols

def symbol_is_adjacent(coords, char_nums):
    line = int(coords[0])
    last_char = int(coords[1])
    for symb in symbols.keys():
        line_symb = int(symb[0])
        char_symb = int(symb[1])
        if ((line_symb >= (line - 1)) and (line_symb <= (line + 1))) and ((char_symb <= (last_char + 1)) and (char_symb >= last_char-char_nums)):
            return True, symb
        else:
            continue
    return False, symb

# get location of all symbols
symbols = get_symbol_locs(input)
print(symbols)

# parse through numbers, see if locations are adjacent to the symbols
for line_num, line in enumerate(input):
    char_list = list(line.strip())
    part_num_list = []
    for char_num, char in enumerate(char_list):
        print(char, char_num)
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and char_num+1 == len(char_list):
            print("last num")
            part_num_list.append(char)
            loc = (line_num, char_num)
            part_num = ("".join([x for x in part_num_list]))
            adjacent, symbol_loc = symbol_is_adjacent(loc, len(part_num_list))
            if adjacent:
                # if so, add to sum
                # print(part_num)
                symbols[symbol_loc].append((int(part_num)))
            part_num_list = []
        elif char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            part_num_list.append(char)
        elif char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and len(part_num_list) > 0:
            loc = (line_num, char_num-1)
            part_num = ("".join([x for x in part_num_list]))
            # print(part_num, part_num_list, loc)
            # parse through numbers, see if locations are adjacent to the symbols
            adjacent, symbol_loc = symbol_is_adjacent(loc, len(part_num_list))
            print(adjacent)
            if adjacent:
                # if so, add to sum
                # print(part_num)
                symbols[symbol_loc].append((int(part_num)))
            part_num_list = []
        else:
            part_num_list = []
            continue

print(symbols)
total = 0
for loc, parts in symbols.items():
    if len(parts) == 2:
        total += (parts[0] * parts[1])
print(total)
