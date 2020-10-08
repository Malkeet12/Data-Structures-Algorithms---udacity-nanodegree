"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def find_max_duration(numbers):
    max_duration = 0
    max_duration_number = None
    for key, value in numbers.items():
        if value > max_duration:
            max_duration = value
            max_duration_number = key

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_duration_number,
                                                                                              max_duration))


def find_number():
    unique_numbers = {}
    for item in calls:
        if item[0] not in unique_numbers:
            unique_numbers[item[0]] = int(item[3])
        elif item[0] in unique_numbers:
            unique_numbers[item[0]] = unique_numbers[item[0]] + int(item[3])

        if item[1] not in unique_numbers:
            unique_numbers[item[1]] = int(item[3])
        elif item[1] in unique_numbers:
            unique_numbers[item[1]] = unique_numbers[item[1]] + int(item[3])

    find_max_duration(unique_numbers)


find_number()

