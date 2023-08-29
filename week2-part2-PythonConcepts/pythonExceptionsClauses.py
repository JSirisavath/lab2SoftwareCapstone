# Try exceptions

city_state = [
    ('Seattle', "WA"),
    ('Portland', "OR"),
    ('San Francisco', "CA"),
]


# print(city_state[5]) # This will be list index out of range


# But if we use the try exceptions clauses, it won't crash

try:
    print(city_state[5])
except:
    print('This index does not exists!')
