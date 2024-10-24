'''
Author: Samuel Ragsdale
Date completed: 24 October 2024
Description: Module 3.1 - 3.6 from the text book Introducing Python 2nd edition
In this program I demonstrate the use of variables and math functions
native to Python. Starting with calculating the number of seconds in
an hour, assigning that number to a variable and using that variable
to work out how many seconds in a day (also in a variable). Finally,
using division to determine how many hours in a day using floating point 
and integer division.
'''

#3.1 - Calculation for seconds in an hour
print(60 * 60)

#3.2 - Previous calculus assigned to variable
seconds_per_hour = 60 * 60

#3.3 - seconds_per_hour used to calculate seconds in a day

print(seconds_per_hour * 24)

#3.4 - previous calculus assigned to a variable

seconds_per_day = seconds_per_hour * 24

#3.5 - floating point division of seconds_per_day by seconds_per_hour

print(seconds_per_day / seconds_per_hour)

#3.6 - same as 3.5 but with integer division instead

print(seconds_per_day // seconds_per_hour)