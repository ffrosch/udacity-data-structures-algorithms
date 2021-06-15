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

from collections import defaultdict

def total_phone_time(calls):
    total_time = defaultdict(int)
    for call in calls:
        caller = call[0]
        receiver = call[1]
        duration = call[-1]

        total_time[caller] += int(duration)
        total_time[receiver] += int(duration)

    return total_time

def longest_phone_time(calls):
    phone_times = total_phone_time(calls)
    max_number = max(phone_times, key=phone_times.get)
    max_time = phone_times.get(max_number)

    return [max_number, max_time]

def test():
    calls = [
        ['(080)2222222', '1401234567', '01-09-2016 01:01:01', '10'],
        ['(080)3333333', '1401234568', '01-09-2016 02:01:01', '20'],
        ['(080)4444444', '1401234568', '01-09-2016 03:01:01', '30'],
    ]

    result_total_phone_time = {
        '(080)2222222': 10,
        '(080)3333333': 20,
        '(080)4444444': 30,
        '1401234567': 10,
        '1401234568': 50,
    }

    total_times = total_phone_time(calls)
    max_time = longest_phone_time(calls)
    assert(total_times == result_total_phone_time)
    assert(max_time == ['1401234568', 50])

# test()
max_time = longest_phone_time(calls)
print(f'{max_time[0]} spent the longest time, {max_time[1]} seconds, on the phone during September 2016.')
