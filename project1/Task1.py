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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_numbers(data, col):
    set_of_numbers = set()
    for row in data:
        set_of_numbers.add(row[col])
    return set_of_numbers


def unique_numbers_total(calls, texts):
    records = calls + texts
    return unique_numbers(records, 0) | unique_numbers(records, 1)


all_numbers = unique_numbers_total(calls, texts)
print(
    f'There are {len(all_numbers)} different telephone numbers in the records.') # noqa
