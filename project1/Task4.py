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
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""


def unique_numbers(data, phone_col):
    output = set()
    for row in data:
        output.add(row[phone_col])
    return output


def only_calling(calls):
    calling = unique_numbers(calls, 0)
    receiving = unique_numbers(calls, 1)
    return calling - receiving


def using_texts(texts):
    sending = unique_numbers(texts, 0)
    receiving = unique_numbers(texts, 1)
    return sending | receiving


def possible_telemarketers(calls, texts):
    only_called = only_calling(calls)
    used_texts = using_texts(texts)
    candidates = only_called - used_texts
    return sorted(candidates)


def test():
    calls = [
        ['(080)1111111', '(080)2222222'],  # only calling
        ['(080)2222222', '1401234567'],  # calling and receiving
        ['(080)3333333', '1401234567'],  # only calling but also sending texts
        # only calling but also receiving texts
        ['(080)4444444', '1401234567'],
    ]

    texts = [
        ['(080)3333333', '1401234567'],  # calls and sends texts
        ['1401234567', '(080)4444444'],  # calls and receives texts
    ]

    assert(only_calling(calls) == set(
        ['(080)1111111', '(080)3333333', '(080)4444444']))
    assert(using_texts(texts) == set(
        ['(080)3333333', '1401234567', '(080)4444444']))
    assert(possible_telemarketers(calls, texts) == ['(080)1111111'])


# test()
print('These numbers could be telemarketers:')
for number in possible_telemarketers(calls, texts):
    print(number)
