with open("adventofcode2023/data/2-long.txt", "r") as f:
    input = f.readlines()


good = 0
for line in input:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_int = int(line.split(":")[0].replace("Game ", ""))
    print(f"start {game_int}")
    sets = [set.strip().split(", ") for set in line.split(":")[1].split(";")]
    # print("sets: ", sets)
    status = "good"
    for set in sets:
        bag = {"red": 12, "green": 13, "blue": 14}
        for item in set:
            num, color = item.split(" ")
            bag[color] -= int(num)
        if any([count for count in bag.values() if count < 0]):
            status = "bad"
    if status == "good":
        print(sets)
        good += game_int
print(good)


