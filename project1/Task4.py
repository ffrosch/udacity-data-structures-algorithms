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

def unique_numbers(data, phone_col):
    output = set()
    for row in data:
        output.add(row[phone_col])
    
    return output

def numbers_calling(calls):
    pass

def numbers_receiving(calls):
    pass

def numbers_texting(texts):
    pass

def only_calling(calls):
    pass

def never_texting(calls, texts):
    pass

def possible_telemarketers(calls, texts):
    pass

