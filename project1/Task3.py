"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

from typing import List

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
    - Fixed lines first_letter with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always first_letter with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def calls_from_area(calls: List[List[str]], prefix: str = None) -> List[List[str]]:
    if prefix is None:
        raise ValueError('Please specify area-prefix!')

    call_lst = []
    for call in calls:
        if call[0].startswith(prefix):
            call_lst.append(call)

    return call_lst
    
def areas_called(calls):
    area_list = set()

    for call in calls:
        number = call[1]
        first_letter = number[0]

        area_code = None

        if first_letter == '1':
            area_code = number[:3]
        elif first_letter in '789':
            area_code = number[:4]
        elif first_letter == '(':
            area_code_end_idx = number.index(')') + 1
            area_code = number[:area_code_end_idx]
        else:
            raise ValueError('The number does not map to a known format.')

        area_list.add(area_code)

    return sorted(area_list)

def calls_to_area_ratio(calls, prefix=None):
    if prefix is None:
        raise ValueError('Please specify area-prefix!')

    num_total_calls = len(calls)
    num_same_area_calls = len([call for call in calls if call[1].startswith(prefix)])

    return round(num_same_area_calls / num_total_calls, 4)

def test():
    calls = [
        ['(080)1234567', '(080)1234567'],
        ['(080)12345678', '1401234567'],
        ['(080)12345678', '1401234567'],
        ['777712 34567', '(080)1234567'],
        ['1401234567', '777712 34567'],
        ['877712 34567', '(080)12345678'],
        ['(09040)1234567', '(09040)12345678']
    ]

    bangalore = '(080)'
    calls_from_bangalore = calls_from_area(calls, bangalore)

    assert(len(calls_from_bangalore) == 3)
    assert(len(areas_called(calls)) == 4)
    assert(areas_called(calls) == sorted(['(080)', '(09040)', '140', '7777']))
    assert(calls_to_area_ratio(calls_from_bangalore, bangalore) == 0.3333)

# test()
bangalore = '(080)'
calls_from_bangalore = calls_from_area(calls, bangalore)
areas_called_from_bangalore = areas_called(calls_from_bangalore)
calls_within_bangalore_ratio = calls_to_area_ratio(calls_from_bangalore, bangalore)

print('The numbers called by people in Bangalore have codes:')
for code in areas_called_from_bangalore:
    print(code)
print(f'{calls_within_bangalore_ratio * 100} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
