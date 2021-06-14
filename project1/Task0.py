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

def first_record(data):
    return data[0]

def last_record(data):
    return data[-1]

def test():
    first_sms = first_record(texts)
    last_call = last_record(calls)

    assert(first_sms == ['97424 22395', '90365 06212', '01-09-2016 06:03:22'])
    assert(last_call == ['98447 62998', '(080)46304537', '30-09-2016 23:57:15', '2151'])

# test()
first_sms = first_record(texts)
last_call = last_record(calls)

print(f'First record of texts, {first_sms[0]} texts {first_sms[1]} at time {first_sms[2]}')
print(f'Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds')
