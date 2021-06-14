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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

texts_first = texts[0]
calls_last = calls [-1]

if __name__ == '__main__':
    print(f'First record of texts, {texts_first[0]} texts {texts_first[1]} at time {texts_first[2]}')
    print(f'Last record of calls, {calls_last[0]} calls {calls_last[1]} at time {calls_last[2]}, lasting {calls_last[3]} seconds')
    