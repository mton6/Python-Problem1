import random

# Set the random seed to 2020 
random.seed(2020)


num_list = []
filter_list = []
# Randomly generate 10,000 numbers between 1000 and 2000
for i in range(10000):
    num = random.randrange(1000,2001)
    num_list.append(num)

# Find all numbers that are even and can be divided by 7
for item in num_list:
    if item % 2 == 0 and item % 7 == 0:
        filter_list.append(item)

# Count the frequency of above numbers
def count_freq(filter_list):
    count_dict = {}

    for items in filter_list:
        count_dict[items]=filter_list.count(items)

# Display numbers in ascending order
    for key, value in sorted(count_dict.items()):

        print("% d % d"%(key, value))

count_freq(filter_list)