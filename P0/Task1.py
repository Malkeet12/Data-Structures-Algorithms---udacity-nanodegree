"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_unique_numbers():
    unique_numbers = []
    # merge two lists
    record = texts + calls
    for item in record:
        if item[0] not in unique_numbers:
            unique_numbers.append((item[0]))
        if item[1] not in unique_numbers:
            unique_numbers.append((item[1]))
    print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))


find_unique_numbers()

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
