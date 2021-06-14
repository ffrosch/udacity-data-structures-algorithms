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

def total_phone_time(calls):
    total_time = dict()
    for call in calls:
        numbers = [call[0], call[1]]
        time = call[3]
        for number in numbers:
            if number not in total_time:
                total_time[number] = int(time)
            else:
                total_time[number] += int(time)
    return total_time

def longest_phone_time(calls):
    # short but cryptic implementation
    # max_time = max(phone_time.items(), key=lambda item: item[1])

    # manual implementation for better interpretability concerning Big O notation
    phone_times = total_phone_time(calls)
    max_time = 0
    max_number = ''
    for number, time in phone_times.items():
        if time > max_time:
            max_time = time
            max_number = number
    return [max_number, max_time]

max_time = longest_phone_time(calls)
print(f'{max_time[0]} spent the longest time, {max_time[1]} seconds, on the phone during September 2016.')
