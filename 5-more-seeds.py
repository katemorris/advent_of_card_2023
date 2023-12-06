with open("data/5-long.txt", "r") as f:
    input = f.read().split("\n\n")

def create_map(commands):
    map = {}
    for command_set in commands:
        dest_start = int(command_set[0])
        source_start = int(command_set[1])
        set_range = int(command_set[2])
        map[(source_start, dest_start)] = set_range
    return map


current_set = {}
for dataset in input:
    # print(dataset)
    if dataset.startswith("seeds:"):
        seeds = [int(s) for s in dataset.replace("seeds: ","").strip().split(" ")]
        
        for seed in seeds:
            current_set[seed] = seed
        continue
    else:
        name, commands_str = dataset.split(":")
        commands = [command_set.split(" ") for command_set in commands_str.strip().split("\n")]
        map = create_map(commands)
        # print(map)
    for seed in seeds:
        print(seed, current_set[seed])
        change_occurred = False
        for (source, dest), range in map.items():
            if change_occurred:
                continue
            print(source, dest, range)
            if current_set[seed] >= source and current_set[seed] <= source + (range - 1):
                print(f"in range {current_set[seed]} is between {source} and {source + (range -1)}")
                diff = current_set[seed] - source
                print(f"diff is {diff} and new data is {dest + diff}")
                current_set[seed] = dest + diff
                change_occurred = True


print(current_set)
print(min(current_set.values()))
