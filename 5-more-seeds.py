with open("data/5-short.txt", "r") as f:
    input = f.read().split("\n\n")

def create_map(commands):
    map = {}
    for command_set in commands:
        dest_start = int(command_set[0])
        source_start = int(command_set[1])
        set_range = int(command_set[2])
        map[(source_start, dest_start)] = set_range
    return map



for dataset in input:
    # print(dataset)
    if dataset.startswith("seeds:"):
        # seeds: 79 14 55 13
        seed_sets = {}
        seed_range = [int(s) for s in dataset.replace("seeds: ","").strip().split(" ")]
        for index, seed_start in enumerate(seed_range[::2]):
            ranges = seed_range[1::2]
            seed_sets[seed_start] = ranges[index]
        # print(seed_sets)
        # {79: 14, 55: 13}
        continue
    else:
        name, commands_str = dataset.split(":")
        commands = [command_set.split(" ") for command_set in commands_str.strip().split("\n")]
        map = create_map(commands)
        # print(map)
    # need to deal with new sets 
    for set_start, set_range in seed_sets.items():
        start_seed = set_start
        end_seed = set_start + (set_range - 1)
        change_occurred = False
        for (source, dest), range in map.items():
            if change_occurred:
                continue
            print(source, dest, range)
            # see if any possible seeds in this set are potentially in the source, edit the range
            if start_seed >= source and end_seed <= source + (range -1):
                # replace all
                diff = start_seed - source
                start_seed = dest + diff
                end_diff = end_seed - (source + (range-1))
                end_seed = dest + end_diff
                change_occurred = True
            elif end_seed <= source + (range -1):
                # new set with new start
                seed_sets[dest] = end_seed - source
                # new set with same start new range
                seed_sets[start_seed] = source - 1
                change_occurred = True
            elif start_seed >= source:
                # break to new set, replace from start_seed to source + range
                diff = (source + (range - 1)) - seed_start
                seed_sets[dest] = dest + diff
                seed_sets[source + range] = end_seed
                change_occurred = True

print(seed_sets)


# print(current_set)
# print(min(current_set.values()))
# 79 - 79+14 (79 - 92)
# 55 - 55+13 (55 - 67)

# seed soil
# 98 - 98+2 (98 - 99)
# 50 - 50+48 (50 - 97)

# start seed = 55
# end seed 98

# pretend set (35-55)
# gets second set for seed soil (50 - 97)
# so 35-49 would be split apart and stay the same 
# 50-55 would be changed to the new destination

# pretend set (9-12)
# seed soil
# 7-10
# 15-51
# 52-53

# same num set = 11-12
# diff set 9-10
# source = 7
# range = 4
# start_seed = 9
# end_seed = 12

