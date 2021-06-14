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

# Sum up phone times
phone_time = dict()
for entry in calls:
    numbers = [entry[0], entry[1]]
    time = entry[3]
    for number in numbers:
        if number not in phone_time:
            phone_time[number] = int(time)
        else:
            phone_time[number] += int(time)


# short but cryptic implementation
# max_time = max(phone_time.items(), key=lambda item: item[1])

# manual implementation
max_time = 0
max_number = ''
for number, time in phone_time.items():
    if time > max_time:
        max_time = time
        max_number = number

print(f'{max_number} spent the longest time, {max_time} seconds, on the phone during September 2016.')
