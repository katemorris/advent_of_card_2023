with open("data/6-long.txt", "r") as f:
    input = f.readlines()

time_data = [int(x) for x in input[0].replace("Time: ", "").strip().split(" ") if x != ""]
distance_data = [int(x) for x in input[1].replace("Distance: ","").strip().split(" ") if x != ""]

def ways_to_win(length, record):
    count_of_ways = 0
    for speed in range(length+1):
        print(speed)
        total_dist = speed * (length - speed)
        if total_dist > record:
            count_of_ways += 1
    return count_of_ways


total = 0
for i in range(len(time_data)):
    length = time_data[i]
    record = distance_data[i]
    count = ways_to_win(length, record)
    if total == 0:
        total = count
    else:
        total *= count

print(total)
