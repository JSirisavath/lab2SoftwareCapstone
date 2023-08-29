# Time Library and their objects

from datetime import datetime, date, time

# Today time
tody = date.today()

# DDate constructor yyyy,m,dd
tomorrow = date(2023, 8, 29)

print(tomorrow)

# Passing date strings in this format
next_week = date.fromisoformat('2023-09-04')

print(next_week)


# Need right exactly now
right_now = datetime.now()

print(right_now)

# Time stamp

print(right_now.timestamp())

# Find a date from a specific timestamp

my_date = datetime.fromtimestamp(3232323232)


print(my_date)
