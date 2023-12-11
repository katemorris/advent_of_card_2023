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
order = {"A":"A", "K":"B", "Q":"C", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M", "J":"N" }
#sort by type
new_hand_dict = {}
hand_types = {"high": [], "one": [], "two": [], "three": [], "house": [], "four": [], "five": []}
for hand in hands.keys():
    cards = list(hand)
    card_type = {}
    for card in cards:
        if card not in card_type.keys():
          card_type[card] = 1
        else:
            card_type[card] += 1
    # deal with Js
    old_hand = hand
    if "J" in card_type.keys():
        print(f"Jacks! in {hand} count of 2s {list(card_type.values()).count(2)}")
        count = card_type["J"]
        if count == 1 and 4 in card_type.values():
            letter = [ct for ct in card_type.keys() if ct != "J"][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 1 and 3 in card_type.values():
            letter = [ct for ct, cc in card_type.items() if ct != "J" and cc == 3][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 1 and list(card_type.values()).count(2) == 2:
            # two pair and one jack, pick the higher of the two pair values
            letters = [ct for ct, cc in card_type.items() if ct != "J" and cc == 2]
            letters_values = [order[letter] for letter in letters]
            letters_values.sort()
            org_ltr = list(order.keys())[list(order.values()).index(letters_values[0])]
            hand = hand.replace("J", org_ltr)
            print(hand)
        elif count == 1 and list(card_type.values()).count(2) == 1:
            # one pair and one jack, make three of a kind
            letter = [ct for ct, cc in card_type.items() if ct != "J" and cc == 2][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif list(card_type.values()) == [1,1,1,1,1]:
            print(f"All different {hand} {card_type}")
            # all different, pick the highest value card
            letters = [ct for ct in card_type.keys() if ct != "J"]
            print(letters)
            letters_values = [order[letter] for letter in letters]
            letters_values.sort()
            org_ltr = list(order.keys())[list(order.values()).index(letters_values[0])]
            hand = hand.replace("J", org_ltr)
            print(hand)
        elif count == 2 and 3 in card_type.values():
            # make the jacks the same as the other three
            letter = [ct for ct in card_type.keys() if ct != "J"][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 2 and list(card_type.values()).count(2) == 2:
            # make the jacks the same as the other two
            letter = [ct for ct, cc in card_type.items() if ct != "J" and cc == 2][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 2 and list(card_type.values()).count(1) == 3:
            # make the jacks the value of the highest card for three
            letters = [ct for ct in card_type.keys() if ct != "J"]
            letters_values = [order[letter] for letter in letters]
            letters_values.sort()
            org_ltr = list(order.keys())[list(order.values()).index(letters_values[0])]
            hand = hand.replace("J", org_ltr)
            print(hand)
        elif count == 3 and 2 in card_type.values():
            # make the jacks the same as the other two
            letter = [ct for ct, cc in card_type.items() if ct != "J" and cc == 2][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 3 and list(card_type.values()).count(1) == 2:
            # make the jacks the same as the highest card
            letters = [ct for ct in card_type.keys() if ct != "J"]
            letters_values = [order[letter] for letter in letters]
            letters_values.sort()
            org_ltr = list(order.keys())[list(order.values()).index(letters_values[0])]
            hand = hand.replace("J", org_ltr)
            print(hand)
        elif count == 4:
            # change to the one card left
            letter = [ct for ct in card_type.keys() if ct != "J"][0]
            hand = hand.replace("J", letter)
            print(hand)
        elif count == 5:
            # change to As
            hand = hand.replace("J", "A")
            print(hand)
    new_hand_dict[hand] = old_hand
    # Redo sets
    cards = list(hand)
    card_type = {}
    for card in cards:
        if card not in card_type.keys():
          card_type[card] = 1
        else:
            card_type[card] += 1
    # sort
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
order = {"A":"A", "K":"B", "Q":"C", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M", "J":"N" }
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
    winnings_hand = new_hand_dict[hand]
    winnings += (rank * int(hands[winnings_hand]))

print(winnings)


# too low 250727973
