with open("data/7-long.txt", "r") as f:
    input = f.readlines()
    hands = {}
    for line in input:
        hand, bid = line.split(" ")
        if hand in hands.keys():
            print("duplicate!")
        else:
            hands[hand] = int(bid)

print(hands)
# sort by type
total_hands = len(hands)
#sort by type
hand_types = {"high": [], "one": [], "two": [], "three": [], "house": [], "four": [], "five": []}
for hand in hands.keys():
    cards = list(hand)
    card_type = {}
    for card in cards:
        if card not in card_type.keys():
          card_type[card] = 1
        else:
            card_type[card] += 1
    if 5 in card_type.values():
        hand_types["five"].append(hand)
    elif 4 in card_type.values():
        hand_types["four"].append(hand)
    elif 3 in card_type.values() and 2 in card_type.values():
        hand_types["house"].append(hand)
    elif 3 in card_type.values():
        hand_types["three"].append(hand)
    elif list(card_type.values()).count(2) == 2:
        hand_types["two"].append(hand)
    elif list(card_type.values()).count(2) == 1:
        hand_types["one"].append(hand)
    elif all(card_type.values()) == 1:
        hand_types["high"].append(hand)
    else:
        print("what kind of hand do you have?")
# print(hand_types)

#sort type members, stronger first
order = {"A":"A", "K":"B", "Q":"C", "J":"D", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M"}
ranked = []
for type, set_hands in hand_types.items():
    print(type)
    print(set_hands)
    hands_index = []
    hand_to_hand_index = {}
    for hand in set_hands:
        hand_index_order = []
        for c in list(hand):
            hand_index_order.append(order[c])
        hand_index = "".join(str(x) for x in hand_index_order)
        print(hand, hand_index)
        hands_index.append(hand_index)
        hand_to_hand_index[hand_index] = hand
    hands_index.sort(reverse=True)
    for hand_index in hands_index:
        ranked.append(hand_to_hand_index[hand_index])

print(ranked)
winnings = 0
for index, hand in enumerate(ranked):
    rank = index + 1
    winnings += (rank * int(hands[hand]))

print(winnings)

# 252,912,235 too low
# 253313241
