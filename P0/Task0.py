"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_message = texts[0]
    sender = first_message[0]
    receiver = first_message[1]
    time = first_message[2]
    print("First record of texts, {} texts {} at time {}".format(sender, receiver, time))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_message = calls[len(calls)-1]
    sender = last_message[0]
    receiver = last_message[1]
    time = last_message[2]
    duration = last_message[3]
    print("Last record of calls, {} calls {} at time {} lasting {} seconds".format(sender, receiver, time, duration))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
