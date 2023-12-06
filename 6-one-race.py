with open("data/6-long.txt", "r") as f:
    input = f.readlines()

time_data = int(input[0].replace("Time: ", "").replace(" ","").strip())
distance_data = int(input[1].replace("Distance: ","").replace(" ","").strip())
# print(time_data, distance_data)
def ways_to_win(length, record):
    count_of_ways = 0
    for speed in range(length+1):
        # print(speed)
        total_dist = speed * (length - speed)
        if total_dist > record:
            count_of_ways += 1
    return count_of_ways


count = ways_to_win(time_data, distance_data)
print(count)
