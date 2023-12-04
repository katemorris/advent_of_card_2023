import re
with open("adventofcode2023/data/1-long.txt", "r") as f:
    input = f.readlines()

total = 0
for line in input:
    line = line.strip()
    print("\nSTART ", line)
    num_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    nums = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]
    num_words_in_string = {}
    for num in nums:
        locs = [m.start() for m in re.finditer(num, line)]
        for n in locs:
            num_words_in_string[n] = num
    sorted_spelled_nums_indexes = list(sorted(num_words_in_string.items()))
    print(sorted_spelled_nums_indexes)
    if sorted_spelled_nums_indexes[0][1] in num_dict.keys():
        first = num_dict[sorted_spelled_nums_indexes[0][1]]
    else:
        first = sorted_spelled_nums_indexes[0][1]
    if sorted_spelled_nums_indexes[-1][1] in num_dict.keys():
        second = num_dict[sorted_spelled_nums_indexes[-1][1]]
    else:
        second = sorted_spelled_nums_indexes[-1][1]
    print(first,second)
    calibv = first + second
    total += int(calibv)
print(total)

# too high 55688
# too low 55680
# too low 54494 
# Issue is in finding all the indexes of all the multiple written words even if they are the same. 
# this works but is not what is expected, they expect us to find the first number at the start and then at the end, nothing more. 
    # num_words_in_string = {}
    # for num_spell in num_spell_dict.keys():
    #     locs = [m.start() for m in re.finditer(num_spell, line)]
    #     for n in locs:
    #         num_words_in_string[n] = num_spell 
    # sorted_spelled_nums_indexes = dict(sorted(num_words_in_string.items()))
    # for index, num_spell in sorted_spelled_nums_indexes.items():
    #     print(f"before {line}")
    #     line = line.replace(num_spell, num_spell_dict[num_spell],1)
    #     print(f"after {line}")
    # print("\nEDITED ", line)
    # num_set = [char for char in list(line) if char in nums_str]
    # print(f"{line}\n{sorted_spelled_nums_indexes}\n{num_set}\n")
    # if len(num_set) == 1:
    #     calibv = num_set[0] + num_set[0]
    # else:
    #     calibv = num_set.pop(0) + num_set.pop(-1)
    # print(calibv, "\nEND")
