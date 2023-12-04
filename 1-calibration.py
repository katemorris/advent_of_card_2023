with open("adventofcode2023/data/1-long.txt", "r") as f:
    input = f.readlines()

total = 0
for line in input:
    # print(line)
    line = line.strip()
    nums_str = [str(num) for num in range(10)]
    num_set = [char for char in list(line) if char in nums_str]
    if len(num_set) == 1:
        calibv = num_set[0] + num_set[0]
    else:
        calibv = num_set.pop(0) + num_set.pop(-1)
    # print(calibv)
    total += int(calibv)
print(total)
    

