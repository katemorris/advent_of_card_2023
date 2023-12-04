with open("adventofcode2023/data/4-long.txt", "r") as f:
    input = f.readlines()

def break_apart_card(line):
    card_str, game_set = line.split(":")
    card_num = int(card_str.replace("Card ","").strip())
    print(card_num)
    raw_winning_nums, raw_your_nums = game_set.split("|")
    winning_nums = [int(x.strip()) for x in raw_winning_nums.split(" ") if x != ""]
    print(winning_nums)
    your_nums = [int(x.strip()) for x in raw_your_nums.split(" ") if x != ""]
    print(your_nums)
    return card_num, winning_nums, your_nums

points = 0
for line in input:
    matches = 0
    card_num, winning_nums, your_nums = break_apart_card(line)
    for yn in your_nums:
        if yn in winning_nums and matches == 0:
            matches = 1
        elif yn in winning_nums:
            matches = matches * 2
    points += matches

print(points)
