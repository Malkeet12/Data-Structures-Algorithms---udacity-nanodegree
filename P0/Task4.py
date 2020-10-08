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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def find_telemarketers():
    telemarketers = []
    for item in calls:
        if item[0] not in telemarketers:
            telemarketers.append(item[0])

    for item in calls:
        if item[1] in telemarketers:
            telemarketers.remove(item[1])

    for item in texts:
        if item[0] in telemarketers:
            telemarketers.remove(item[0])
        if item[1] in telemarketers:
            telemarketers.remove(item[1])
    telemarketers.sort()
    print("These numbers could be telemarketers:")

    for item in telemarketers:
        print(item)


find_telemarketers()
