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

def process_card(cards_won, repeats=1):
    while repeats >= 1:
        matches = 0
        for yn in your_nums:
            if yn in winning_nums:
                matches += 1
        for c in range(matches):
            add = c+1
            new_card = card_num + add
            if new_card in cards_won.keys():
                cards_won[new_card] += 1
            else:
                cards_won[new_card] = 1
        repeats -= 1
    return cards_won

cards_won = {}
card_nums = []
for line in input:
    card_num, winning_nums, your_nums = break_apart_card(line)
    card_nums.append(card_num)
    if card_num in cards_won.keys():
        cards_won[card_num] += 1
        print(card_num, cards_won[card_num])
        cards_won = process_card(cards_won, cards_won[card_num])
    else:
        print("no key")
        cards_won[card_num] = 1
        process_card(cards_won, cards_won[card_num])

total_cards = 0
for cn, s in cards_won.items():
    if cn in card_nums:
        total_cards += s
print(total_cards)
