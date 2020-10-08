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
    unique_numbers = set()
    # merge two lists
    record = texts + calls
    for item in record:
        unique_numbers.add(item[0])
        unique_numbers.add(item[1])
    print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))


find_unique_numbers()

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
