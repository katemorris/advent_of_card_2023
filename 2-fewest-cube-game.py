with open("adventofcode2023/data/2-long.txt", "r") as f:
    input = f.readlines()


total = 0
for line in input:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_int = int(line.split(":")[0].replace("Game ", ""))
    print(f"start {game_int}")
    sets = [set.strip().split(", ") for set in line.split(":")[1].split(";")]
    status = "good"
    bag = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        empty_bag = {"red": 0, "green": 0, "blue": 0}
        for item in set:
            num, color = item.split(" ")
            empty_bag[color] += int(num)
        for color, num in empty_bag.items():
            if bag[color] < num:
                bag[color] = num
    power = bag["red"] * bag["blue"] * bag["green"]
    total += power
print(total)
        



